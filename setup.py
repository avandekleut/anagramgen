from distutils.core import setup
setup(
  name = 'anagramgen',         # How you named your package folder (MyLib)
  packages = ['anagramgen'],   # Chose the same as "name"
  version = '0.1.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Generate multi-word anagrams from any corpus.',   # Give a short description about your library
  author = 'Alexander Van de Kleut',                   # Type in your name
  author_email = 'avandekleut@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/avandekleut/anagramgen',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/avandekleut/anagramgen/archive/v_01.tar.gz',    # I explain this later on
  keywords = ["ANAGRAM", "ANAGRAMS", "GENERATOR", "SOLVER", "FINDER"],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha', 'Intended Audience :: Developers',
    'Topic :: Utilities',    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
