# Quotes Search Tool

A command-line search engine for [quotes.toscrape.com](https://quotes.toscrape.com).

## Setup

```bash
python3 -m pip install -r requirements.txt
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

## Testing

Run all tests:

```bash
PYTHONPATH=. python3 -m unittest discover -s tests -q
```

Run test file:

```bash
python3 -m unittest -v tests.test_crawler
```
```bash
python3 -m unittest -v tests.test_indexer
```
```bash
python3 -m unittest -v tests.test_search
```