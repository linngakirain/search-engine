# Quotes Search Tool

A command-line search engine that crawls [quotes.toscrape.com](https://quotes.toscrape.com), builds an inverted index with word positions, and provides a CLI to search for exact phrases.

## Installation & Setup
### Clone or download the repository
```bash
git clone https://github.com/linngakirain/search-engine.git
```

```bash
cd search_tool
```

### Install dependencies
```bash
pip install -r requirements.txt
```

## Run The App

```bash
python3 -m src.main
```

Then use these commands in the shell:

- `build`
- `load`
- `print <word>`
- `find <word or phrase>`
- `exit`

Examples:
```
> build
Building index... Please wait.
Build complete.

> load
Load complete.

> print nonsense
Inverted index for 'nonsense':
  https://quotes.toscrape.com/page/2/ -> positions [398]
  https://quotes.toscrape.com/page/7/ -> positions [293]

> find good
Pages containing 'good':
  https://quotes.toscrape.com/page/1/
  https://quotes.toscrape.com/page/2/
  https://quotes.toscrape.com/page/3/
  https://quotes.toscrape.com/page/6/
  https://quotes.toscrape.com/page/7/
  https://quotes.toscrape.com/page/9/

> find good friends
Pages containing 'good friends':
  https://quotes.toscrape.com/page/2/

> find hand upon my chest is my hand
Pages containing 'hand upon my chest is my hand':
  https://quotes.toscrape.com/page/3/

> exit
```

## Testing

### Run all tests:

```bash
PYTHONPATH=. python3 -m unittest discover -s tests -q
```

### Run test file:

```bash
python3 -m unittest -v tests.test_crawler
```
```bash
python3 -m unittest -v tests.test_indexer
```
```bash
python3 -m unittest -v tests.test_search
```