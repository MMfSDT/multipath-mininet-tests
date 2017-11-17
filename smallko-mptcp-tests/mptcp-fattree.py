#!/usr/bin/env python
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import Link, TCLink, Intf
from subprocess import Popen, PIPE
from mininet.log import setLogLevel
import sys

if '__main__' == __name__:
    setLogLevel('info')
    net = Mininet(link=TCLink)
    #key = "net.mptcp.mptcp_enabled"
    #value = 1
    #p = Popen("sysctl -w %s=%s" % (key, value),
    #        shell=True, stdout=PIPE, stderr=PIPE)
    #stdout, stderr = p.communicate()
    #print "stdout=", stdout, "stderr=", stderr

    K = int(sys.argv[1])
    print "Generating topology for K =",K

    print "Naming convention"
    print "Host:               h<pod><i><j>"
    print "Edge switch:        se<pod><i>"
    print "Aggregate switch:   sa<pod><i>"
    print "Core switch:        sc<i><j>"

    hosts = [[[
    net.addHost('h'+str(pod)+str(i)+str(j))
    for i in range(K/2)]
    for j in range(K/2)]
    for pod in range(K)]

    edge = [[
    net.addHost('se'+str(pod)+str(i))
    for i in range(K/2)]
    for pod in range(K)]

    agg = [[
    net.addHost('sa'+str(pod)+str(i))
    for i in range(K/2)]
    for pod in range(K)]

    core = [[
    net.addHost('sc'+str(i)+str(j))
    for j in range(K/2)]
    for i in range(K/2)]

    linkopt = {'bw': 10}

    #host to edge
    for pod in range(K):
        for i in range(K/2):
            for j in range(K/2):
                net.addLink(hosts[pod][i][j],edge[pod][i],cls=TCLink,**linkopt)

    #edge to aggregate
    for pod in range(K):
        for i in range(K/2):
            for j in range(K/2):
                net.addLink(edge[pod][i],agg[pod][j],cls=TCLink,**linkopt)

    #aggregate to core
    for pod in range(K):
        for i in range(K/2):
            for j in range(K/2):
                net.addLink(agg[pod][i],core[i][j],cls=TCLink,**linkopt)

    net.build()

    # r1.cmd("ifconfig r1-eth0 0")
    # r1.cmd("ifconfig r1-eth1 0")
    # r1.cmd("ifconfig r1-eth2 0")
    # r1.cmd("ifconfig r1-eth3 0")
    # h1.cmd("ifconfig h1-eth0 0")
    # h1.cmd("ifconfig h1-eth1 0")
    # h2.cmd("ifconfig h2-eth0 0")
    # h2.cmd("ifconfig h2-eth1 0")
    # r1.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")
    # r1.cmd("ifconfig r1-eth0 10.0.0.1 netmask 255.255.255.0")
    # r1.cmd("ifconfig r1-eth1 10.0.1.1 netmask 255.255.255.0")
    # r1.cmd("ifconfig r1-eth2 10.0.2.1 netmask 255.255.255.0")
    # r1.cmd("ifconfig r1-eth3 10.0.3.1 netmask 255.255.255.0")
    # h1.cmd("ifconfig h1-eth0 10.0.0.2 netmask 255.255.255.0")
    # h1.cmd("ifconfig h1-eth1 10.0.1.2 netmask 255.255.255.0")
    # h2.cmd("ifconfig h2-eth0 10.0.2.2 netmask 255.255.255.0")
    # h2.cmd("ifconfig h2-eth1 10.0.3.2 netmask 255.255.255.0")
    # h1.cmd("ip rule add from 10.0.0.2 table 1")
    # h1.cmd("ip rule add from 10.0.1.2 table 2")
    # h1.cmd("ip route add 10.0.0.0/24 dev h1-eth0 scope link table 1")
    # h1.cmd("ip route add default via 10.0.0.1 dev h1-eth0 table 1")
    # h1.cmd("ip route add 10.0.1.0/24 dev h1-eth1 scope link table 2")
    # h1.cmd("ip route add default via 10.0.1.1 dev h1-eth1 table 2")
    # h1.cmd("ip route add default scope global nexthop via 10.0.0.1 dev h1-eth0")
    # h2.cmd("ip rule add from 10.0.2.2 table 1")
    # h2.cmd("ip rule add from 10.0.3.2 table 2")
    # h2.cmd("ip route add 10.0.2.0/24 dev h2-eth0 scope link table 1")
    # h2.cmd("ip route add default via 10.0.2.1 dev h2-eth0 table 1")
    # h2.cmd("ip route add 10.0.3.0/24 dev h2-eth1 scope link table 2")
    # h2.cmd("ip route add default via 10.0.3.1 dev h2-eth1 table 2")
    # h2.cmd("ip route add default scope global nexthop via 10.0.2.1 dev h2-eth0")
    CLI(net)
    net.stop()
