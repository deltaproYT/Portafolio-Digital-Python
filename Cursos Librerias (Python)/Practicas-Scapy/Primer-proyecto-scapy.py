import tkinter as tk
from tkinter import scrolledtext
from scapy.all import ARP, Ether, send, srp, IP, TCP


pkt = IP(dst="8.8.8.8")/TCP(dport=80)
print(pkt.summary())
