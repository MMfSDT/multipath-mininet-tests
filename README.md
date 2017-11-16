# Multipath TCP tests in Mininet

Tests assume a preconfigured system with `linux-mptcp`, `mininet`, and `wireshark`.

## Contents
`tcp-send-receive/`
* Basic send/receive code in Python. Initializes handshake (SYN-ACK handshake), sends `<message | *>`, then closes the connection (FIN-RST handshake).