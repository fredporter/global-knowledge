---
title: "uDos Device Display Capability Standards & Calculation Engine"
version: "1.0.0"
status: "canonical"
tags: [standards, display, hardware, geometry, gridcore, prose, sonic-screwdriver]
---

# uDos Device Display Capability Standards & Calculation Engine

This standard governs how **Sonic Screwdriver**, **CMMint**, **HomeNest**, and **Apple Silicon Macs** evaluate target hardware displays to determine optimal character grid capacity, reading measures, Zen viewport scaling, and animated BOB memory budgets.

---

## 1. Hardware Tiers & Target Profiles

| Tier | Profile ID | Primary Target Hardware | Common Resolutions | Aspect | Primary Interaction | Optimal Surface Mode |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Tier 1: Sovereign Desktop** | `desktop_hd` | Apple Silicon Mac (M-Series) | 1440×900, 1920×1080, 2560×1440 | 16:10 / 16:9 | Keyboard & Trackpad | `prose_reader` / Multi-pane |
| **Tier 2A: Revived POS / Kiosk** | `pos_kiosk` | Recycled Touch Terminals (via Sonic Screwdriver USB) | 800×600, 1024×768 | 4:3 | Touch-first (min 52px targets) | `zen_card` (Typeform flow) |
| **Tier 2B: Revived Retro CRT / PC** | `retro_crt` | Older Intel Macs, PCs, CRT monitors | 640×480, 1024×768, 1280×1024 | 4:3 / 5:4 | Keyboard & Mouse | `zen_card` / `teletext_mode7` |
| **Tier 3: 10-Foot Console** | `ten_foot_tv` | Living Room TV, Classroom Projector | 1280×720 (720p), 1920×1080 (1080p) | 16:9 | DPAD / Gamepad / Remote | `ten_foot_deck` (Marp style) |
| **Tier 4: Beacon / Mobile Client** | `mobile_portal` | Smartphone / Tablet visiting captive portal | 375×667, 390×844, 768×1024 | 9:16 / 3:4 | Touch scroll & tap | `zen_card` / Mobile Prose |

---

## 2. Dynamic Display Capability Calculation Engine

Given a physical screen with resolution $W \times H$ (device pixels) and optional DPI/scale, the system computes:

### A. GridCore Geometry Capacity
- **Atomic Dot**: $1\text{ dot} = 4\times 4\text{ px}$.
- **Square Cell Register** ($8\times 8\text{ px} = 2\times 2\text{ dots}$):
  $$\text{Cols}_{\text{sq}} = \left\lfloor \frac{W}{8} \right\rfloor, \quad \text{Rows}_{\text{sq}} = \left\lfloor \frac{H}{8} \right\rfloor$$
- **Tall Cell Register** ($12\times 20\text{ px} = 3\times 5\text{ dots}$):
  $$\text{Cols}_{\text{tall}} = \left\lfloor \frac{W}{12} \right\rfloor, \quad \text{Rows}_{\text{tall}} = \left\lfloor \frac{H}{20} \right\rfloor$$
- **Super-Cell Tile** ($24\times 40\text{ px} = 6\times 10\text{ dots}$):
  $$\text{SuperCols} = \left\lfloor \frac{W}{24} \right\rfloor, \quad \text{SuperRows} = \left\lfloor \frac{H}{40} \right\rfloor$$
- **Teletext Standard Fit**: Teletext Mode 7 requires $40\text{ cols} \times 25\text{ rows} = 480 \times 500\text{ px}$ at 1× dot scale ($960 \times 1000\text{ px}$ at 2×). If $W < 480$ or $H < 500$, Mode 7 requires viewport scroll or scaling.

### B. Prose Line Measure Capacity
- Reading measure rule: 1 standard character measure $\approx 0.6 \times \text{font\_size}$.
- At standard 16px body font ($1\text{ ch} \approx 9.6\text{ px}$):
  $$\text{Measure}_{\text{ch}} = \left\lfloor \frac{W}{9.6} \right\rfloor$$
- **Layout Decision**:
  - If $\text{Measure}_{\text{ch}} < 50\text{ch}$ ($W < 480\text{ px}$): Single mobile column (35ch–40ch, 100% width).
  - If $50\text{ch} \le \text{Measure}_{\text{ch}} < 90\text{ch}$ ($480\text{ px} \le W < 864\text{ px}$): Centered single column (clamped to 50ch–65ch).
  - If $\text{Measure}_{\text{ch}} \ge 90\text{ch}$ ($W \ge 864\text{ px}$): **Optimal Zen Prose Measure** (strictly clamped to **70ch–72ch** / $\approx 680\text{ px}$ centered with letterbox margins). Never stretch text across wider displays.

### C. Tri-Mode Zen Viewport Scale Factor
To eliminate layout distortion, Zen views render inside a calibrated, non-stretching letterbox/pillarbox canvas:
- **Reference Aspects**:
  - $4:3$ Reference Box: $800 \times 600\text{ px}$
  - $16:9$ Reference Box: $1280 \times 720\text{ px}$
- **Target Selection**:
  $$\text{TargetAspect} = \begin{cases} 4:3 & \text{if } W / H < 1.5 \\ 16:9 & \text{if } W / H \ge 1.5 \end{cases}$$
- **Proportional Scale Factor $S$**:
  $$S = \min\left(\frac{W}{W_{\text{ref}}}, \frac{H}{H_{\text{ref}}}\right)$$
- The container renders at $(W_{\text{ref}} \cdot S) \times (H_{\text{ref}} \cdot S)$ centered within the display.

### D. BOB (Blitter Object) Memory Budget
- Maximum BOB dimensions: $128 \times 128\text{ px}$. Typical dimensions: $64 \times 64\text{ px}$ or $32 \times 32\text{ px}$.
- Memory footprint:
  $$\text{RAM}_{\text{bob}} = W \times H \times N_{\text{frames}} \times 1\text{ byte}$$
- Recommended maximum RAM footprint: $\le 128\text{ KB}$ per animated BOB.
- Recommended maximum disk / payload size: $\le 60\text{ KB}$ per looping GIF asset.
