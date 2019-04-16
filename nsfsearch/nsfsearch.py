__copyright__ = """

    Copyright 2019 Samapriya Roy

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

"""
__license__ = "Apache 2.0"
import requests
import json
import os
import sys
import csv
import argparse
lpath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(lpath)

# Looks for keywords and searches the database
def wordsearch(wordlist):
    for items in wordlist:
        r=requests.get('https://api.nsf.gov/services/v1/awards.json?keyword='+str(items))
        try:
            for award in json.loads(r.text)['response']['award']:
                print('NSF award ID: '+str(award['id']))
                print('PI: '+str(award['piFirstName'])+' '+str(award['piLastName']))
                print('Awardee Name: '+str(award['awardeeName'].strip()))
                print('Funds Obligated $'+str("{:,}".format(int(award['fundsObligatedAmt']))))
                print('Date '+str(award['date']))
                print('')
        except Exception as e:
            print(e)
def wordsearch_from_parser(args):
    wordsearch(wordlist=[args.wordlist])

# Exports keyword searches to csv file
def searchexp(wordlist,outfile):
    with open(outfile, 'wb') as csvfile:
        writer=csv.DictWriter(csvfile, fieldnames=["id", "first_name", "last_name",
        "awardee_name","funds_obligated", "date"], delimiter=',')
        writer.writeheader()
    i=1
    for items in wordlist:
        r=requests.get('https://api.nsf.gov/services/v1/awards.json?keyword='+str(items))
        try:
            for award in json.loads(r.text)['response']['award']:
                print('Processing award '+str(i))
                i=i+1
                with open(outfile,'a') as csvfile:
                    writer=csv.writer(csvfile,delimiter=',',lineterminator='\n')
                    writer.writerow([str(award['id']),str(award['piFirstName']),str(award['piLastName']),
                        str("{:,}".format(int(award['fundsObligatedAmt']))),str(award['date'])])
                csvfile.close()
        except Exception as e:
            print(e)


def searchexp_from_parser(args):
    searchexp(wordlist=[args.wordlist],outfile=args.file)


# Searches award details using ID
def idsearch(ids):
        r=requests.get('https://api.nsf.gov/services/v1/awards/'+str(ids)+'.json')
        try:
            for award in json.loads(r.text)['response']['award']:
                print('NSF award ID: '+str(award['id']))
                print('PI: '+str(award['piFirstName'])+' '+str(award['piLastName']))
                print('Awardee Name: '+str(award['awardeeName'].strip()))
                print('Funds Obligated $'+str("{:,}".format(int(award['fundsObligatedAmt']))))
                print('Date '+str(award['date']))
                print('')
        except Exception as e:
            print(e)


def idsearch_from_parser(args):
    idsearch(ids=args.ids)


# Searches award details & print outcome using ID
def outcome(ids):
        r=requests.get('https://api.nsf.gov/services/v1/awards/'+str(ids)+'/projectoutcomes.json')
        try:
            for award in json.loads(r.text)['response']['award']:
                print('NSF award ID: '+str(award['id']))
                print('PI: '+str(award['projectOutComesReport']).replace("\n", "").replace("\t\t", "\t").strip())
                print('')
        except Exception as e:
            print(e)


def outcome_from_parser(args):
    outcome(ids=args.ids)


def main(args=None):
    parser = argparse.ArgumentParser(description='NSF Awards API Simple CLI')

    subparsers = parser.add_subparsers()

    parser_wordsearch = subparsers.add_parser('keysearch', help='Searches for all projects with keywords')
    required_named=parser_wordsearch.add_argument('--wordlist', nargs='+', help='Send comma seperated keywords', default=None)
    parser_wordsearch.set_defaults(func=wordsearch_from_parser)

    parser_searchexp = subparsers.add_parser('export', help='Searches for all projects with keywords & export')
    required_named=parser_searchexp.add_argument('--wordlist', nargs='+', help='Send comma seperated keywords', default=None)
    required_named=parser_searchexp.add_argument('--file', help='Outfile CSV file with results', default=None)
    parser_searchexp.set_defaults(func=searchexp_from_parser)

    parser_idsearch = subparsers.add_parser('idsearch', help='Search using project ID')
    required_named=parser_idsearch.add_argument('--ids', help='Project ID', default=None)
    parser_idsearch.set_defaults(func=idsearch_from_parser)

    parser_outcome = subparsers.add_parser('result', help='Project outcome based on ID')
    required_named=parser_outcome.add_argument('--ids', help='Project ID', default=None)
    parser_outcome.set_defaults(func=outcome_from_parser)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
