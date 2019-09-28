from anagramgen import anagramgen
with open('anagramgen/corpuses/top-5k.txt', 'r') as file:
    corpus = [line.strip() for line in file.readlines()]
gen = anagramgen.AnagramGenerator(corpus)
print("\n".join([" ".join(anagram) for anagram in gen.generate("wonderland")]))
