#!/usr/bin/env python3
from argparse import ArgumentParser
from requests import get, exceptions
from json import loads

STARRED_REQUEST = 'http://api.github.com/users/{user}/starred'
STATUS_CODE_NOT_FOUND = 404
STATUS_CODE_OK = 200
DEFAULT_REPO_PARAMETERS = ('full_name', 'stargazers_count')


def main():
    parser = ArgumentParser(
        description='Simple utility to get github user starred repositories')
    parser.add_argument('login', type=str, help='User github login')
    parser.add_argument('-t', '--timeout', default=4, type=float,
                        help='Timeout to response')
    parser.add_argument('-repo_parameters', type=str, nargs='+',
                        default=DEFAULT_REPO_PARAMETERS,
                        help='Repository parameters to get')
    args = parser.parse_args()
    response = get_response(args.login, args.timeout)
    if response is None:
        print('Timeout exceeded')
        return
    if response.status_code == STATUS_CODE_NOT_FOUND:
        print('User with such login is not found')
        return
    if response.status_code != STATUS_CODE_OK:
        print('Incorrect response status code: {}. Should be {}'.
            format(response.status_code, STATUS_CODE_OK))
        return
    print('Starred repositories of user {}:'.format(args.login))
    print('Format: {}\n'.
        format(' '.join(args.repo_parameters)))
    print('\n'.join(get_repos_parameters(response.text, args.repo_parameters)))
            


def get_response(login, timeout):
    try:
        return get(STARRED_REQUEST.format(user=login), timeout=timeout)
    except exceptions.ConnectTimeout:
        return None


def get_repos_parameters(response_body, repo_parameters):
    for repo in loads(response_body):
        yield ' '.join(
            str(repo.get(parameter, 'None')) for parameter in repo_parameters)


if __name__ == "__main__":
    main()
