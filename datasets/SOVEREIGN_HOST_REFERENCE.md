# Sovereign host reference

Status: required product contract; adapter behavior must be qualified separately.

The host operating system is authoritative for time and timezone. uDOS does not add clock-sync, NTP or timezone-setting daemons. Users configure host time settings through their operating system. Applications read host time through their platform APIs and must test timezone-sensitive behavior.

Location is separately permissioned and may be unavailable, stale or unsupported. Reading host time does not grant location access. Use qualified host adapters and explicit permission; do not claim automatic location inheritance.

Offline maps and spatial operations should use verified local reference packs without requiring constant web synchronization. Product code owns calculations and mapping algorithms. Existing product seeds and host timezone databases remain authoritative until a tested migration selects verified replacements. This source proposal does not demonstrate complete offline mapping support.

External retrieval is an explicit intake operation with provenance and a selected destination. Review updates before canon promotion. No map updater daemon or duplicate host reference service is introduced.
