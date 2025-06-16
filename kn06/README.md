# A)
Subnet: 172.31.100.0/20
Private IP Master: 172.31.100.1
Public IP Master: 54.88.69.67
Private IP Node1: 172.31.100.2
Public IP Node1: 13.216.61.123
Private IP Node2: 172.31.100.3
Public IP Node2: 52.1.176.51

![screenshot workers](assets/2025-06-16-14-13-00.png)
# B)
## Workers von anderem Node aus
![node1](assets/2025-06-16-14-15-10.png)
## microk8s status
![microk8s status](assets/2025-06-16-14-17-49.png)
```bash
# microk8s läuft gerade
microk8s is running
# Ab 3 Nodes ist es highly availible und vor single failures geschützt
high-availability: yes
  # Alle unsere Nodes sind als master hinzugefügt werden
  datastore master nodes: 172.31.100.1:19001 172.31.100.2:19001 172.31.100.3:19001
  # Aktuell befinden sich keine Nodes im Standby modus
  datastore standby nodes: none
```
## Node entfernen
### Schritt 1
![leave](assets/2025-06-16-14-24-48.png)
### Schritt 2
![remove](assets/2025-06-16-14-26-45.png)
## Node als Worker hinzufügen
![status](assets/2025-06-16-14-31-46.png)
Nicht mehr highly availiable, weil der Worker kein Control Panel hat.
## Get nodes
### Worker
![master](assets/2025-06-16-14-34-44.png)
### Node2 (Worker)
![node2 (worker)](assets/2025-06-16-14-36-59.png)
Weil Worker Nodes kein Control Panel haben, können sie diese Commands nicht ausführen.
# Unterschied microk8s und microk8s kubectl
## microk8s
Damit kann man seinen Cluster administrieren
## microk8s kubectl
Kubectl gibt es auch ausserhalb von microk8s. Damit kann man seine Cluster verwalten.
