#!/usr/bin/env python

""" Compile every Java source under src/ together, reproducing the Makefile's
`javac -Xlint:all <sources> -d bin`. File arguments are ignored -- javac is run
once over the whole source set. """

import glob
import os
import subprocess
import sys

OUT = "bin"


def main():
    """ main entry point """
    sources = sorted(glob.glob(os.path.join("src", "**", "*.java"), recursive=True))
    if not sources:
        return
    os.makedirs(OUT, exist_ok=True)
    sys.exit(subprocess.call(["javac", "-Xlint:all", *sources, "-d", OUT]))


if __name__ == "__main__":
    main()
