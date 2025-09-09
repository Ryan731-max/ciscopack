
  int tunnel 1
  ip address 10.10.10.1 255.255.255.252
  tunnel source s0/0/0
  tunnel destination 209.165.10.2

  int tunnel 1
  ip address 10.10.10.2 255.255.255.252
  tunnel source s0/1/1
  tunnel destination 209.165.200.2

