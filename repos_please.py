#!/usr/bin/env python3

import json
import requests
import sys


def get_info(user_name):
    get_link = 'https://api.github.com/users/{}/repos'.format(user_name)
    get_source = requests.get(get_link)
    get_status = get_source.status_code

    if get_status == 200:
        repos = json.loads(get_source.text)
        repo_list = []

        for repo in repos:
            repo_list.append(repo['url'])
            repos_url = []

            for url in repo_list:
                repos_url.append(
                    url[len(get_link):])
                print(repos_url[-1])

    else:
        return 'Your username is not available or unaccessed, please try again'


def main():

    try:
        user = sys.argv[1]
    except IndexError:
        print('Well, type something and try again, or shut me down please')

    return get_info(user)

if __name__ == '__main__':
    main()
