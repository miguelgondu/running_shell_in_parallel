# A hack for running shell scripts in parallel

This is a massive hack to run a `.sh` script in parallel using Python.

Write a logic inside `make_sh.py` to write a `to_run.sh` script with all the experiments that you want to run.

After that, you can run

```
python pool.py to_run.sh --processes=n
```

where n is the amount of processors you want to devote to the process. It will literally run all lines in to_run.sh, but in parallel.

# Requisites

- Python >3.6
- `pip install click`
