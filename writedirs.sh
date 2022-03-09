#!/bin/bash

find / '(' -type f -o -type d ')' \
       '(' '(' -user  `whoami` -perm -u=w ')' -o \
           '(' -group `whoami` -perm -g=w ')' -o \
           '('               -perm -o=w ')' ')' -print
