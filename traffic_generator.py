import requests
import random

from .util import ANYSCALE_CLI_TOKEN

CLUSTER_TOKEN = requests.get("https://api.anyscale.com/v0/clusters/ses_8KpYmRqRMft6dfD4yGcVJGhk", cookies={"cli_token": ANYSCALE_CLI_TOKEN}).json()["result"]["access_token"]

for i in range(10000):
    res = requests.get("https://dashboard-ses-ahkbbyeefqkafvexvr4ms86u.anyscale-internal-hsrczdm-0000.anyscale-test-staging.com/serve/ImageRecognitionService", cookies={"anyscale-token": CLUSTER_TOKEN})
    print(random.choice(["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]))
    #print(res.content)
