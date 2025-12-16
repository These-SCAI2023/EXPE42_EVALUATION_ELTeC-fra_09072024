import os
from subprocess import Popen
import glob
# for year in range(2011, 2025):
for year in range(1990, 1999):
  # if len(glob.glob(f"./papers_OCR_{year}/*"))>5:
  #   print(year, "DONE")
  #   continue
  # cmd = f"python -m PyPaperBot --query='OCR DPI resolution quality' --scholar-pages=10  --min-year={year} --max-dwn-year={year} --dwn-dir='./papers_Land-Degradation_{year}' --scihub-mirror='https://sci-hub.do'"
  # cmd_list = ["python","-m","PyPaperBot","--query='OCR DPI resolution quality'","--scholar-pages=1",f"--min-year={year}",f"--max-dwn-year={year}",f"--dwn-dir=./papers_Land-Degradation_{year}","--scihub-mirror='https://sci-hub.do'"]
  cmd = f"python -m PyPaperBot --query=OCR 300 DPI recommended --scholar-pages=10  --min-year={year} --max-dwn-year={year} --dwn-dir='./papers_Land-Degradation_{year}' --scihub-mirror='https://sci-hub.do'"
  cmd_list = ["python", "-m", "PyPaperBot", "--query=OCR 300 DPI recommended", "--scholar-pages=1",
              f"--min-year={year}", f"--max-dwn-year={year}", f"--dwn-dir=./papers_Land-Degradation_{year}",
              "--scihub-mirror='https://sci-hub.do'"]
  print(cmd)
  # Popen(cmd_list)
  Popen(cmd_list).wait()
  break
