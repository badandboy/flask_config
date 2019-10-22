#!/usr/bin/env bash
ps -ef|grep manage.py|grep -v grep|awk '{print $2}'|xargs kill
nohup python3 manage.py >> manage.log &