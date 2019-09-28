# anagram-generator

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

`anagram-generator` is a minimal python package that lets you generate multi-word anagrams from any corpus. This package is written in pure python and has no dependencies. See `anagram-generator/writeup/writeup.pdf` to learn how it works (**tries** and clever sorting of partially generated anagrams), or read the source code at `anagram-generator/anagram-generator.py`. Example corpuses are in `anagram-generator/corpuses`. 

### Installation

Installation is easy using `pip`.

```sh
$ pip install anagramgen
```

### Example
```python
from anagramgen import AnagramGenerator
with open('corpuses/top-5k.txt', 'r') as file:
    corpus = [line.strip() for line in file.readlines()]
gen = AnagramGenerator(corpus)
gen.generate("wonderland")
```
returns

```python
[['do', 'lend', 'warn'], 
 ['down', 'land', 're'], 
 ['draw', 'lend', 'on'], 
 ['draw', 'lend', 'no'], 
 ['dawn', 'lend', 'or'], 
 ['end', 'old', 'warn'], 
 ['end', 'lawn', 'rod'], 
 ['end', 'land', 'row'], 
 ['lend', 'nod', 'war'], 
 ['lend', 'nod', 'raw'], 
 ['lawn', 'nod', 'red'], 
 ['land', 'wonder'], 
 ['land', 'own', 'red'], 
 ['land', 'now', 'red'], 
 ['land', 'new', 'rod'], 
 ['a', 'drown', 'lend'], 
 ['and', 'lend', 'row']]
```
