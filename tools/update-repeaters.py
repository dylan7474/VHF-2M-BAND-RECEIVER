#!/usr/bin/env python3
"""Regenerate repeaters.js from the RSGB ETCC list at ukrepeater.net.

Keeps 2m repeaters only. Run from the repo root:  python3 tools/update-repeaters.py
"""
import csv, io, json, urllib.request, datetime

URL = "https://ukrepeater.net/csvcreate1.php"

raw = urllib.request.urlopen(URL, timeout=30).read().decode("latin-1")
rows = []
for r in csv.DictReader(io.StringIO(raw)):
    if r["band"].strip().upper() != "2M":
        continue
    try:
        out_mhz, in_mhz = float(r["TX"]), float(r["RX"])
        lat, lon = float(r["lat"]), float(r["lon"])
    except ValueError:
        continue
    if not 144 <= out_mhz <= 146:
        continue
    rows.append([
        r["repeater"].strip(),              # callsign
        round(out_mhz, 5),                  # output: what you listen to
        round(in_mhz, 5),                   # input: what users transmit on
        r["ctcss/cc"].strip(),              # CTCSS tone (analogue) or colour code
        r["where"].strip().title(),         # town
        r["region"].strip(),                # RSGB region code
        round(lat, 3), round(lon, 3),
        r["Modes"].strip(),                 # A=analogue D=D-STAR M=DMR F=Fusion N=NXDN
        r["channel"].strip(),               # e.g. RV58
    ])
rows.sort(key=lambda x: (x[1], x[0]))

today = datetime.date.today().isoformat()
with open("repeaters.js", "w") as f:
    f.write(f"// UK 2m repeaters from ukrepeater.net (RSGB ETCC), fetched {today}.\n")
    f.write("// Regenerate with: python3 tools/update-repeaters.py\n")
    f.write("// [callsign, outputMHz, inputMHz, ctcss, town, region, lat, lon, modes, channel]\n")
    f.write(f'const REPEATERS_UPDATED = "{today}";\n')
    f.write("const REPEATERS = [\n")
    f.write(",\n".join(json.dumps(r, ensure_ascii=False) for r in rows))
    f.write("\n];\n")
print(f"wrote {len(rows)} repeaters")
