# nsfsearch: NSF Awards API Simple CLI
This is an application based on the [NSF Awards API](https://www.research.gov/common/webapi/awardapisearch-v1.htm). While the NSF award search tool is great, this is useful to get some quick reports and statistics on NSF awards. It also does act as a quick search and ideally as NSF updates the API this tool will be updated to reflect changes.

## Table of contents
* [Installation](#installation)
* [Getting started](#getting-started)
* [nsfsearch: NSF Awards API Simple CLI](#nsfsearch-nsf-awards-api-simple-cli)
    * [keysearch](#keysearch)
    * [export](#export)
    * [idsearch](#idsearch)
    * [result](#result)

## Installation
This assumes that you have native python & pip installed in your system, you can test this by going to the terminal (or windows command prompt) and trying

```python``` and then ```pip list```


To install **nsfsearch: Simple CLI for Google Home & Mini** you can install using two methods.

```pip install nsfsearch```

or you can also try

```
git clone https://github.com/samapriya/nsfsearch.git
cd nsfsearch
python setup.py install
```
For Linux use sudo or try ```pip install nsfsearch --user```.

Installation is an optional step; the application can also be run directly by executing nsfsearch.py script. The advantage of having it installed is that nsfsearch can be executed as any command line tool. I recommend installation within a virtual environment. If you don't want to install, browse into the nsfsearch folder and try ```python nsfsearch.py``` to get to the same result.


## Getting started

As usual, to print help:

```
NSF Awards API Simple CLI

positional arguments:
  {keysearch,export,idsearch,result}
    keysearch           Searches for all projects with keywords
    export              Searches for all projects with keywords & export
    idsearch            Search using project ID
    result              Project outcome based on ID

optional arguments:
  -h, --help            show this help message and exit
```

To obtain help for specific functionality, simply call it with _help_ switch, e.g.: `nsfsearch result -h`. If you didn't install nsfsearch, then you can run it just by going to *nsfsearch* directory and running `python nsfsearch.py [arguments go here]`

## nsfsearch NSF Awards API Simple CLI
The tool is based on curret NSF [award search API](https://www.research.gov/common/webapi/awardapisearch-v1.htm) and is subject to change in the future.

### keysearch
This allows you to get all awards based on a keyword search, you can pass keywords as comman seperated value and it iterates through the list and prints the result to console. Usage is simply

```
usage: nsfsearch keysearch [-h] [--wordlist WORDLIST [WORDLIST ...]]

optional arguments:
  -h, --help            show this help message and exit
  --wordlist WORDLIST [WORDLIST ...]
                        Send comma seperated keywords
```

### export
This tool exports the keysearch results to a csv file, instead of printing it out on the console.

```
usage: nsfsearch export [-h] [--wordlist WORDLIST [WORDLIST ...]]
                        [--file FILE]

optional arguments:
  -h, --help            show this help message and exit
  --wordlist WORDLIST [WORDLIST ...]
                        Send comma seperated keywords
  --file FILE           Outfile CSV file with results
```

### idsearch
Looks at specific NSF project using project id.

```
usage: nsfsearch idsearch [-h] [--ids IDS]

optional arguments:
  -h, --help  show this help message and exit
  --ids IDS   Project ID
```

### result
Get any project outcome results as reported by NSF using project id.

```
usage: nsfsearch result [-h] [--ids IDS]

optional arguments:
  -h, --help  show this help message and exit
  --ids IDS   Project ID
```
