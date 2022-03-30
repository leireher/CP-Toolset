# Competitive Programming Toolset

This repo aims to collect useful implementations of common algorithms in the
Competitive Programming domain. This algorithms are collected as a library
so that they can be easily used during a contest.

__*NOTE*__: these algorithms should only be used in Competitive Programming, do not 
use them in production as they may be full of bad coding practices.

## Useful Resources

- [UVa Online Judge](https://onlinejudge.org/index.php): Online automated judge 
for programming problems, its problem archive has over 4300 problems.
- [HackerRank](https://www.hackerrank.com/): Website that provides challenges
for several different domains such as Algorithms, Mathematics, SQL, 
Functional Programming, AI, and more. HackerRank also provides the ability for 
users to submit applications and apply to jobs by solving company-sponsored 
coding challenges.
- [Codeforces](https://codeforces.com/): One of the most active websites that 
hosts Competitive Programming contests. After the contests problem editorials
are published by problem authors, it is a good way of getting started in 
Competitive Programming.

## Unofficial ICPC Judge usage

The unofficial judge [icpc_judge.py](icpc_judge.py) can be used to validate solutions
to problems from past ICPC editions. The folder holding the test cases of the problems
should have the following structure:

```
root/
├── sample/
|   ├── sample01.in
|   ├── sample01.ans
|   ├── ...
|   ├── sampleN.in
|   └── sampleN.ans
├── secret/
|   ├── test01.in
|   ├── test01.ans
|   ├── ...
|   ├── testN.in
|   └── testN.ans
└── problem.yaml (Optional)
```

The file `problem.yaml` specifies the limits under which the proposed solution should
run. This unofficial judge only takes into account the time and memory limits. A sample
`problem.yaml` is the following:

```yaml
source: Southwestern Europe Regional Contest (SWERC) 2020-2021
source_url: https://swerc.eu/
author: Silviu Maniu
license: cc by-sa
name: Restaurants
uuid: L
limits:
  validation_time: 3
  memory: 3072
```

The `validation_time` field indicates the maximum amount of seconds that the solution
can take to generate the output (defaults to 1 second), and the `memory` field indicates
the maximum amount of memory in MiB that the solution can allocate (defaults to 2048 MiB).

The actual judge usage can be seen by running `python3 icpc_judge.py -h`.

__NOTE__: Usually, past ICPC contest problem test cases can be downloaded from they
corresponding official website. These test cases follow the folder structure explained
above. [Here](https://swerc.eu/2020/theme/problems/swerc.zip) you can download the full 
problemset with test cases for the 2020 SWERC edition.
