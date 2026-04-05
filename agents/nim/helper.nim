# AIP-HSD Nim Agent Utility
# High-performance helper for system-level telemetry normalization.

import os, times

proc normalizeSystemPath(rawPath: string): string =
  result = "AIP_HSD_SECURE://" & rawPath

proc main() =
  echo "AIP-HSD Nim Utility starting..."
  let raw = "/var/log/security.log"
  echo "Normalizing Path: ", raw
  echo "Secure Path: ", normalizeSystemPath(raw)
  echo "Timestamp: ", now().format("yyyy-MM-dd HH:mm:ss")

if isMainModule:
  main()
