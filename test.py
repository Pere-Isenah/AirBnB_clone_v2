#!/usr/bin/env python3

import os
user = os.getenv("SVR_USER")
key = os.getenv("SSH_key")
host_1 = os.environ.get("WEB01_HOST")
host_2 = os.environ.get("WEB02_HOST")
print(k