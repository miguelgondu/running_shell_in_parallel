'''
This script runs in parallel all the lines in to_run.sh.

It can be called like this:

python pool.py to_run.sh --processes=n

where n is the amount of cpus you want to devote to the
process.
'''

import click
import multiprocessing
import subprocess


def simulate(line):
    subprocess.call([line.strip()], shell=True)


@click.command()
@click.argument('filename', type=click.File(mode='r'))
@click.option('--processes', type=int, default=None)
@click.option('--dry/--no-dry', default=False)

def main(filename, processes, dry):
    pool = multiprocessing.Pool(processes=processes)

    pool.map(simulate, filename)

if __name__ == '__main__':
    main()
