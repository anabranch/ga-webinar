from fastapi import FastAPI
from ray import serve

serve.start(detached=True)

app = FastAPI()

@serve.deployment(route_prefix="/")
@serve.ingress(app)
class HelloWorld:
    @app.get("/query")
    def hello(self):
        return f"Hello world!"
    
    @app.get("/healthcheck")
    def healthcheck(self):
        return

HelloWorld.deploy()



# import requests
# import random
# CLUSTER_TOKEN="08ac92ec-d056-4127-a5f4-bd821e918133"
# for i in range(10000):
#     res = requests.get("https://dashboard-ses-ahkbbyeefqkafvexvr4ms86u.anyscale-internal-hsrczdm-0000.anyscale-test-staging.com/serve/ImageRecognitionService", cookies={"anyscale-token": CLUSTER_TOKEN})
#     print(random.choice(["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]))
#     #print(res.content)