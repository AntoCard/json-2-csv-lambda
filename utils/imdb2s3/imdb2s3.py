#!/usr/bin/env python3

import requests
import argparse
import json
import boto3
import sys

#api_key = 'edf47c635088b6c3b147f2870a99e228'


def get_movie_info(api_key, movie_title):
    imdb_url = 'https://api.themoviedb.org/3/search/movie/?api_key='
    r = requests.get(imdb_url + api_key + '&query=' + movie_title)
    json_request = r.json()
    print(json_request)
    if json_request['total_results'] == 0:
        print('No results found for query')
        sys.exit(0)
    else:
        return json_request


def upload_to_s3_ia(bucket_name, file_name, content):
    s3 = boto3.resource('s3')
    file_name = file_name.replace('+', '')
    s3.Object(bucket_name, 'json/' + file_name + '.json').put(Body=json.dumps(content),
                                                               StorageClass='STANDARD_IA')


def main():
    parser = argparse.ArgumentParser(description='Search for a movie in IMDB and upload the json result to S3')

    parser.add_argument('--bucket', '-b', dest='bucket', required=True,
                        help='bucket where to upload json')
    parser.add_argument('--key', '-k', dest='key', required=True,
                        help='imdb api key')
    parser.add_argument('--movie', '-m', dest='movie', required=True,
                        help='movie name (use + instead of spaces')

    if len(sys.argv[1:]) == 0:
        parser.print_help()
        parser.exit()

    args = parser.parse_args()

    bucket_name = args.bucket
    api_key = args.key
    movie_title = args.movie

    movie_info = get_movie_info(api_key, movie_title)
    upload_to_s3_ia(bucket_name, movie_title, movie_info)


if __name__== "__main__":
  main()
