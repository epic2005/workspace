# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Host, HostGroup
import hashlib

try:
    import json
except ImportError,e:
    import simplejson as json

def collect(request):
    req = request
    if req.POST:
        vendor = req.POST.get('vendor')
        product = req.POST.get('product')
        sn = req.POST.get('sn')
        hostname = req.POST.get('hostname')
        osbit = req.POST.get('osbit')
        osver = req.POST.get('osver')
        cpu_model = req.POST.get('cpu_model') 
        cpucores = req.POST.get('cpucores')
        cpu_num = req.POST.get('cpu_num')
        memory = req.POST.get('memory')
        ipaddr = req.POST.get('ip')
        #ipaddrs = req.POST.get('ipaddr')
        m = hashlib.md5()
        m.update(req.POST.get('uuid'))
        uuid = m.hexdigest()

        try:
            host = Host.objects.get(hostname=hostname)
        except:    
            host = Host()
        host.vendor = vendor
        host.product = product
        host.sn = sn
        host.hostname = hostname 
        host.osbit = osbit
        host.osver = osver
        host.cpumodel = cpu_model
        host.cpucores = cpucores
        host.cpunum = cpu_num
        host.memory = memory
        host.ipaddr = ipaddr
        host.uuid = uuid
        host.save()
        
        return HttpResponse("ok")
    else:
        return HttpResponse("no post data")

def gethosts(req):
    d=[]
    hostgroups = HostGroup.objects.all()

    for hg in hostgroups:
        ret_hg = {'hostgroup':hg.name,'members':[]}
        members = hg.members.all()
        for h in members:
            ret_h = {'hostname':h.hostname,'ipaddr':h.ipaddr,}
            ret_hg['members'].append(ret_h)
        d.append(ret_hg)
    ret = {'status':0, 'data':d,'message':'OK'}
    return HttpResponse(json.dumps(ret))

def gethoststxt(req):
    d = ""
    hostgroups = HostGroup.objects.all()
    for hg in hostgroups:
        members =  hg.members.all()
        for h in members:
            ips = ','.join([i.ipaddr for i in h.ipaddr_set.all()])
            d += "%s %s %s\n" % (hg.name, h.hostname, ips)
    return HttpResponse(d)

