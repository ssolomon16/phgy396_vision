import os, sys
import pandas as pd
import numpy as np
import zipfile
import urllib
from urllib.request import urlopen
from io import BytesIO

url = 'https://figshare.com/ndownloader/files/27039812'
#gazebase_zip = urlopen(url)

zip_path, _ = urllib.request.urlretrieve(url)
with zipfile.ZipFile(zip_path, "r") as f:
    f.extractall('gb_data2')
f.close()

#with urlopen(url) as f:
#    with zipfile.ZipFile(BytesIO(f.read())) as zfile:
#        zfile.extractall('gazebase_data')
#f.close()

#with zipfile.ZipFile("gazebase.zip", 'r') as zip_ref:
#    zip_ref.extractall(gazebase_data)
