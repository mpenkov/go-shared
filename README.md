# go-shared

This project demonstrates a problem with building shared libraries from Go source using Github Actions.

The library source contains a single function, called cNoop, which does nothing.
I then build this library into a shared object using Github Actions.
The workflow is [here](https://github.com/mpenkov/go-shared/blob/master/.github/workflows/build.yml).
Nothing fancy, just a `go build -buildmode=c-shared`.

The problem is that the resulting shared object is extremely slow to use.
Calling the cNoop function 1 million times from e.g. Python takes nearly 30s.

In contrast, if I build the shared object locally on my machine, the same task (1 million calls to cNoop) takes a fraction of a second.

## TL;DR

```bash
$ RUNPY_LIB_PATH=builds/lib.so.gha2 python run.py  # github actions, build 2
made 1000000 calls in 33.91s
$ RUNPY_LIB_PATH=builds/lib.so.local python run.py # local build
made 1000000 calls in 0.26s
```

## Questions

- Why is the runtime so dramatically slower for the shared object built by Github Actions?
- How can I get Github Actions to build shared objects that aren't so slow to use?
