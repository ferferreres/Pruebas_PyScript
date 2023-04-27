import pandas as pd

df = pd.read_csv('res/Dependencies.csv')

csv = Element('csv')
csv.write(df.shape)