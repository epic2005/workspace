#!/usr/bin/env python

import urllib, urllib2
from collector import IDCServer

def mkpost(urldata):
    api_url = "http://127.0.0.1:8000/api/collect"
    post_url = urllib.urlencode(urldata)
    ret = urllib2.urlopen(api_url,post_url)
    return ret.read()

def main():
	urldata = {}
	idc = IDCServer()
	urldata['vendor'] = idc.idc_vendor()
	urldata['product'] = idc.idc_product()
	urldata['sn'] = idc.idc_sn()
	urldata['hostname'] = idc.idc_hostname()
	urldata['osbit'] =  idc.idc_osbit()
	urldata['ip'] =  idc.idc_ips()
	urldata['cpucores'],urldata['cpu_num'],urldata['cpu_model'] =  idc.idc_cpu()
	urldata['memory'] =  idc.idc_memory()
	urldata['osver'] =  idc.idc_osver()
	urldata['uuid'] =  idc.idc_uuid()
	print mkpost(urldata)

if __name__ == '__main__':
	main()
