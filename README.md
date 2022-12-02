# JWSTapipy
[![CodeQL](https://github.com/malinkinsa/jwstapipy/actions/workflows/codeql-analysis.yml/badge.svg?branch=master)](https://github.com/malinkinsa/jwstapipy/actions/workflows/codeql-analysis.yml)
![PyPI - Downloads](https://img.shields.io/pypi/dm/jwstapipy)
![PyPI](https://img.shields.io/pypi/v/jwstapipy)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/jwstapipy)

Simple python library for access to data from jwstapi.com

- [JWSTapipy](#jwstapipy)
  - [Description](#description)
  - [Get JWSTapipy](#get-jwstapipy)
  - [Examples](#Examples)
    - [Get list of programs](#get-list-of-programs)
    - [Get part of program data by ID](#get-part-of-program-data-by-id)

## Description
JWSTapipy is a simple python library to work with data provided by the site [https://jwstapi.com/](https://jwstapi.com/)
The site provides James Webb Space Telescope data. Data is sourced from MAST, processed and exposed through API.

Tested on JWST API version 0.0.15

## Get JWSTapipy
```python
pip install jwstapipy
```

## Examples
### Get list of programs
```python
import asyncio
import jwstapipy

async def main(api_key):
    jwst = JwstAPI(api_key)
    
    programs = await jwst.get_programs_list()
    print(programs)

if __name__ == "__main__":
    asyncio.run(main('api_key'))
```

### Get part of program data by ID
```python
import asyncio
import jwstapipy

async def main(api_key):
    jwst = JwstAPI(api_key)
    
    program_data = await jwst.get_program_data(program_id=2731, first_page=1, last_page=2)
    print(program_data)

if __name__ == "__main__":
    asyncio.run(main('api_key'))
```
