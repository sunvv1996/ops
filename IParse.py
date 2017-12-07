# -*- coding: utf-8 -*-
#!/usr/bin/env python

from IPy import IP

ips_s = input(u'请输入ip或ip段:')

ips = IP(ips_s)
if len(ips) > 1:
    print('net: %s'% ips.net())
    print('netmask: %s'% ips.netmask())
    print('broadcast: %s'% ips.broadcast())
    print('reverse address: %s'% ips.reverseNames()[0])
    print('subnet: %s'% len(ips))
else:
    print('reverse address: %s' % ips.reverseNames()[0])

print('hexadecimal:%s'% ips.strHex())
print('binary:%s'% ips.strBin())
print('iptype:%s'% ips.iptype())