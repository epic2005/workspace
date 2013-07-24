#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

data = {'class':['web','web-monitor']}
a = yaml.dump(data, explicit_start=True,default_flow_style=False)
print a
