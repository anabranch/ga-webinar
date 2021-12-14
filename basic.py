import ray
import random

ray.init()

@ray.remote
def inner_task():
    print("Starting Simulation")
    for x in range(10000000):
        5 + 5
    print("Terminating Simulation, Result: "+ random.choice(["Success", "Failure"]))
    return 1


@ray.remote
def starter_task():
    results = []
    print("Starting Simulation Manager")
    for x in range(5):
        task = inner_task.remote()
        results.append(task)
    print("Terminating Simulation Manager")
    return ray.get(results)


results = []
print("Running all Simulations")
for x in range(1000):
    task = starter_task.remote()
    results.append(task)


ray.get(results)
