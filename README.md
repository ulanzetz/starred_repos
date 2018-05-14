# Starred Repositories
Simple utility to get github user starred repositories

Usage:
```
starred_repos.py [-h] [-t TIMEOUT] [-repo_parameters REPO_PARAMETERS [REPO_PARAMETERS ...]] login
```


Positional arguments:
```
  login                 User github login
```

Optional arguments:
```
  -h, --help      show this help message and exit
  -t TIMEOUT, --timeout TIMEOUT     Timeout to response
  -repo_parameters REPO_PARAMETERS [REPO_PARAMETERS ...]      Repository parameters to get
```

Examples:
```
python3 starred_repos.py torvalds
Starred repositories of user torvalds
Format: full_name stargazers_count

torvalds/linux 58638
Subsurface-divelog/subsurface 1367
```
```
python3 starred_repos.py torvalds -repo_parameters name watchers_count language
Starred repositories of user torvalds:
Format: name watchers_count language

linux 58638 C
subsurface 1367 C++
```
