---
title: "Sovereign Host as the Reference Point"
version: "1.0.0"
status: "canonical"
tags: [architecture, clock, gps, reference, host]
---

# Sovereign Host as the Point of Reference

## 1. Principle of Non-Duplication

Modern host operating systems (macOS, Linux Mint, BSD) already manage accurate real-time clock (RTC) hardware, network time protocol (NTP) synchronization, and geolocation services.

- **uDos does NOT run its own clock-sync daemon or NTP client.**
- **uDos does NOT implement an internal timezone setter or date adjuster.**
- **The local host machine is the sovereign source of truth.**

## 2. Setting Date, Time, and Location

If the date, time, timezone, or location requires adjustment:
1. The user configures their host operating system directly (e.g. macOS System Settings -> Date & Time, or Linux Mint Date/Time applet).
2. All uDos applications and services automatically inherit the host's system time (`datetime.now(timezone.utc)` and `time.tzname`) and location services on the next operation.

## 3. Offline Maps & Spatial APIs

Mapping layers and spatial coordinate engines (GridCore 2D algebra, Teletext coordinate mapper) run entirely offline against local datasets in `~/Public/global-knowledge/datasets/` and `~/Public/global-knowledge/reference/`.

External tools (such as `BrowserUI`) can scrape, enhance, and download updated map tiles or point-of-interest data into the local vault as an intentional intake action, without requiring uDos to continuously ping external mapping APIs to function.
