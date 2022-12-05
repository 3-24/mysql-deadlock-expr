import subprocess as sp

REPT = 10

def average_time():
    with open("result.txt", 'r') as f:
        l = list(map(float, f.readlines()))
    
    #assert (len(l) == REPT)

    return sum(l) / len(l)

for n in range (2, 401):
    for _ in range (REPT):
        sp.run(f"python3.10 main.py {n}", shell=True)
    
    t = average_time()
    print(n, t)
    with open("total.txt", "a") as f:
        f.write(f"{n} {t}\n")

    sp.run("rm result.txt", shell=True)