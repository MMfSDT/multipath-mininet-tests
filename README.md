# Multipath TCP tests in Mininet

Tests assume a preconfigured system with `linux-mptcp`, `mininet`, and `wireshark`.

## Contents
`tcp-send-receive/`
* Basic send/receive code in Python. Initializes handshake (SYN-ACK handshake), sends `<message | *>`, then closes the connection (FIN-RST handshake).

`smallko-mptcp-tests/`
* Basic MPTCP topology setup. Uses a host for a router in the middle. Directly lifted from [here](http://csie.nqu.edu.tw/smallko/sdn/mptcp-test.htm). Topology for `simple1` and `simple2` is as follows.

![1]

![2]

[1]: http://csie.nqu.edu.tw/smallko/sdn/mptcp-test.files/image012.png
[2]: http://csie.nqu.edu.tw/smallko/sdn/mptcp-test.files/image012.png