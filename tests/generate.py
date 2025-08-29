#!/usr/bin/env python3
import os, random; random.seed(48)
def w(name, alumnos):
    os.makedirs("tests", exist_ok=True)
    with open(f"tests/input_{name}.txt","w") as f:
        f.write(str(len(alumnos))+"\\n")
        for (nom,a,b,c) in alumnos:
            f.write(f"{nom} {a:.2f} {b:.2f} {c:.2f}\\n")
    best=None
    for (nom,a,b,c) in alumnos:
        avg=(a+b+c)/3.0
        if best is None or avg>best[1]: best=(nom,avg)
    open(f"tests/output_{name}.txt","w").write(f"{best[0]} {best[1]:.2f}\\n")
def main():
    w("min", [("Ana",5.0,4.5,4.8)])
    n=10**5; alumnos=[(f"a{i}", (i%50)/10.0+3.0, ((i*7)%50)/10.0+3.0, ((i*13)%50)/10.0+3.0) for i in range(n)]
    w("max", alumnos)
    rnd=[(f"u{i}", random.uniform(0.0,5.0), random.uniform(0.0,5.0), random.uniform(0.0,5.0)) for i in range(1234)]
    w("rnd", rnd)
if __name__=="__main__": main()
