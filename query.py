# 

import requests
import random

ANYSCALE_CLI_TOKEN = "sss_uEVZtRx7vuP36LjAxmtvhuAW"

CLUSTER_TOKEN = requests.get("https://api.anyscale.com/v0/clusters/ses_8KpYmRqRMft6dfD4yGcVJGhk", cookies={"cli_token": ANYSCALE_CLI_TOKEN}).json()["result"]["access_token"]

for i in range(1000):
    res = requests.get("https://serve-session-8kpymrqrmft6dfd4ygcvjghk.i.anyscaleuserdata.com/query", cookies={"anyscale-token": CLUSTER_TOKEN})
    print(res.status_code)