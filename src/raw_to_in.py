import glob
import os
import pandas as pd
import numpy as np

RAW_DIR = '../raw'
IN_DIR = '../in'

rawSessions = [dI for dI in os.listdir(RAW_DIR) if os.path.isdir(os.path.join(RAW_DIR, dI))]


for rawSession in rawSessions:
 print(rawSession)
 convertedDierctory = IN_DIR + '/' + rawSession
 if not os.path.exists(convertedDierctory):
  os.makedirs(convertedDierctory)
 sessionFiles = glob.glob(RAW_DIR + '/' + rawSession + '/*.csv')
 print(sessionFiles)


 for sessionFile in sessionFiles:
  read = pd.read_csv(sessionFile, header=None)
  readX = read.iloc[:, :-1].values
  aClass = int(read.iloc[0,-1])
  print('Read class ', aClass, ' ',  readX.shape)

  readXNp = np.array(readX).reshape(readX.shape[0]*8, 8)
  convertedFileName = sessionFile.replace('/raw/', '/in/')

  pd.DataFrame(readXNp).to_csv(path_or_buf = convertedFileName, header=[aClass]*8, index=False)

