# Netzwerke
```bash
# Netzwerk erstellen
docker network create tbz

# Container im default Network erstellen
docker run --name busybox1 busybox:latest
docker run --name busybox2 busybox:latest

# Container im tbz Network erstellen 
docker run --name busybox3 --net tbz busybox:latest
docker run --name busybox4 --net tbz busybox:latest
```

## IP Adressen
1. 172.17.0.4
2. 172.17.0.5
3. 172.18.0.2
4. 172.18.0.3

## Aufgaben Busybox1
```bash
# Welcher Default-Gateway ist eingetragen? Welcher Container hat den gleichen?
docker inspect # -> 172.17.0.1
# ping busybox2
ping busybox2 # -> ping: bad address 'busybox2'
# ping busybox3
ping busybox3 # -> ping: bad address 'busybox3'
# ping IP-von-busybox2
ping 172.17.0.5 # -> 14 packets transmitted, 14 packets received, 0% packet loss
# ping IP-von-busybox3
ping 172.18.0.2 # -> 63 packets transmitted, 0 packets received, 100% packet loss
```
## Aufgaben Busybox3
```bash
# Welcher Default-Gateway ist eingetragen? Welcher Container hat den gleichen?
docker inspect # -> 172.18.0.1
# ping busybox1
ping busybox1 # -> ping: bad address 'busybox1'
# ping busybox4
ping busybox4 # -> 7 packets transmitted, 7 packets received, 0% packet loss
# ping IP-von-busybox1
ping 172.17.0.4 # -> 8 packets transmitted, 0 packets received, 100% packet loss
# ping IP-von-busybox4
ping 172.18.0.3 # -> 6 packets transmitted, 6 packets received, 0% packet loss
```
## Unterschiede
Beim default Network kann man nicht mit dem Namen auf den Container zugreifen,
mit dem custom Network schon.
Das tbz Network muss beim Start des Container explizit gesetzt werden.
## Vergleich kn02
### In welchem Netzwerk befanden sich die beiden Container?
Im default Network
### Wieso konnten die miteinander reden?
Weil sie gelinkt wurden.
