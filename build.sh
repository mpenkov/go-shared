#!/usr/bin/env bash
set -euxo pipefail
export LD_LIBRARY_PATH=builds
go build -o builds/liblocal.so -buildmode=c-shared
mv builds/liblocal.h builds/local.h

#
# give ldd a helping hand so it can find the shared object build by GHA
#
if [ ! -f builds/libgha2.so ]; then
    ln -s builds/lib.so.gha2 builds/libgha2.so
fi

gcc cmd/run/main.c -Ibuilds -Lbuilds -llocal -o bin/runlocal
gcc cmd/run/main.c -Ibuilds -Lbuilds -lgha2 -o bin/rungha2
