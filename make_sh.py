'''
This script creates a to_run.sh file which is to
be run using pool.py.

Let's say you're running a python script named
training.py, and it accepts several flags (e.g.
--lr, --attr). You could write something like

with open("to_run.sh", "w") as to_run
    for lr in [0.01, 0.001]:
        for attr in range(40):
            to_run.write(f"python training.py --lr={lr} --attr={attr}")

At the end of all this, you should have a to_run.sh file
with all the lines you intended to run. This is the one that
goes to pool.py.
'''
from itertools import product

def main():
    with open("to_run.sh", mode="w") as to_run:
        for a, b in product(range(10), range(10)):
            to_run.write(f"python example.py --a={a} --b={b}\n")

if __name__ == '__main__':
    main()
