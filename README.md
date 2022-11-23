# pandas_profiling

Pandas-profiling with PyScript support.

![Pandas Profiling Logo Header](https://pandas-profiling.ydata.ai/docs/assets/logo_header.png)

## build phik

```BASH
git clone https://github.com/alitrack/PhiK
cd PhiK
python setup.py bdist_wheel --universal
cp dist/phik-0.12.2-py2.py3-none-any.whl ..
```

## build htmlmin

```BASH
git clone https://github.com/mankyd/htmlmin
cd htmlmin
python setup.py bdist_wheel --universal
cp dist/htmlmin-0.1.12-py2.py3-none-any.whl ..
```

## Load local packages and local paths

```HTML
    - ./htmlmin-0.1.12-py2.py3-none-any.whl
    - ./phik-0.12.2-py2.py3-none-any.whl
    - pandas-profiling
    - imagehash
    - paths:
        - ex.py
```

## No module named '_multiprocessing' issue

A workaround is to monkypatch the _multiprocessing module:

```PYTHON
  import sys
  sys.modules['_multiprocessing'] = object
  from multiprocessing.pool import ThreadPool
```

for details, please visit [here](https://github.com/pyodide/pyodide/issues/1603).