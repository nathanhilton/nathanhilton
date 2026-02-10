#!/usr/bin/env bash
cd "$(dirname "$0")"
mkdir -p out
status=0
latexmk -pdf -jobname=resume-nathan-hilton -output-directory=out main.tex || status=$?
if [[ -f out/resume-nathan-hilton.pdf ]]; then
  mv out/resume-nathan-hilton.pdf .
  echo "Built resume-nathan-hilton.pdf"
fi
exit $status
