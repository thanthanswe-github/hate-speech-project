import pandas as pd
import sys
from tqdm import tqdm
import json

from CrowdTangleExportCommentsTools import HsleCandidateGenerationUtils as hsle
import HateSpeechData as hsd
from glob import glob


from pathlib import Path

files = glob('../../hsle/data/exportcomments-outputs/*/processed/merged.csv')
files.sort()
print(len(files))

with open('../../hsle/src/_current_data_.json') as f:
  data = json.load(f)
  daterange =data['daterange']


for f in tqdm(files):
	split_file = str(f).split('/')[5]
	if split_file==daterange:
		file_check =glob(f)
		data = hsd.HateSpeechData(file_check)
		data.run()


