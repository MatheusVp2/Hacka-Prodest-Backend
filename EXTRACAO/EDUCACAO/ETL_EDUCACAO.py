import pandas as pd
import numpy as np
import json

df = pd.read_csv('./educacao.csv', sep=";")

keys = df.to_dict(orient='records')[0].keys()

for key in keys:
    try:
        df.loc[df[key].isna(), key] = None
        df[key] = df[key].apply( lambda x: None if np.isnan(x) else x )
    except Exception as error:
        print(error)
        print("Chave: ", key)
        continue

dados_json = df.to_dict(orient="records")

with open("./educacao.json", "w", encoding="UTF-8") as fs:
    json.dump(dados_json, fs, ensure_ascii=False, indent=4)