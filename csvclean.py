#!/usr/bin/env python3
"""CSV cleaner: trim whitespace, hapus duplikat baris."""
import csv, sys
src, dst = sys.argv[1], sys.argv[2]
seen, rows = set(), []
with open(src, newline="") as f:
      for row in csv.reader(f):
                row = [c.strip() for c in row]
                key = tuple(row)
                if key in seen: continue
                          seen.add(key); rows.append(row)
        with open(dst, "w", newline="") as f:
              csv.writer(f).writerows(rows)
          print(f"{len(rows)} rows (deduped)")
