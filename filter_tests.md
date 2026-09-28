# Network Traffic Filtering Test Record

## 1. Environment & IP Mapping
- **Server IP:** `192.168.10.100` (Service: SSH / Port 22)
- **Staff Subnet:** `192.168.10.0/24`
- **Guest Subnet:** `192.168.20.0/24`
- **External IP:** `203.0.113.45`

## 2. Firewall Rules (`iptables`)
```bash
# Flush existing rules
sudo iptables -F INPUT

# Allow loopback interface
sudo iptables -A INPUT -i lo -j ACCEPT

# Allow established/related connections
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Rule 3a: Explicitly block guest network to server
sudo iptables -A INPUT -s 192.168.20.0/24 -d 192.168.10.100 -j DROP

# Rule 3b: Permit authorized staff network access to SSH (Port 22)
sudo iptables -A INPUT -p tcp -s 192.168.10.0/24 --dport 22 -d 192.168.10.100 -j ACCEPT

# Rule 3c: Block all other inbound access to SSH (Port 22)
sudo iptables -A INPUT -p tcp --dport 22 -j DROP
