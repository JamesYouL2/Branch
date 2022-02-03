# %%
import json
import pandas as pd
import requests

# %%
url = "https://randomuser.me/api/?results=500"

# %%
response = requests.get(url)
data = response.json()

# %%
df=pd.json_normalize(data["results"])

# %%
df.rename(columns=lambda x: x.replace(".", "_"), inplace=True)

# %%
df.to_csv("data.csv")

# %%



