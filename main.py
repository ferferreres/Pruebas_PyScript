import pandas as pd
from pyodide.http import open_url

url = 'https://raw.githubusercontent.com/ferferreres/Pruebas_PyScript/main/res/Dependencies.csv'
url_content = open_url(url)

df = pd.read_csv(url_content)
print(df['functional_domain'])