# Ethos Lending - test task

## How to run tests

You need to run commands below:

1. Install dependencies that are required to run autotests.

```
$ pip install -r requirements.txt
```

2. Run the command to run automation test with HTML-report generation. HTML report can be found in the current directory.

```
$ pytest test --html=report.html
```

3. If you don't need HTML-report, than run the following command.

```
$ pytest test
```

## About test task

More information about service: https://httpbin.org/

Used to create autotests:

`HTTP Methods`
Testing different HTTP verbs:
GET: /get (The request's query parameters.)
POST: /post (The request's POST parameters.)

`Auth`
Auth methods:
GET: /basic-auth/{user}/{passwd} (Prompts the user for authorization using HTTP Basic Auth.)

`Dynamic data`
Generates random and dynamic data
GET: /stream/{n} (Stream n JSON responses)
This service has a bug. Service can not return more than 100 rows
For example:
1. https://httpbin.org/stream/7 (return 7 rows)
1. https://httpbin.org/stream/100 (return 100 rows)
1. https://httpbin.org/stream/150 (return 100 rows) !!!bug!!!