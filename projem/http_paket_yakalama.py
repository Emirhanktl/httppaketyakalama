#!/usr/bin/env python3
from scapy.all import sniff, TCP, Raw

def paket_yakala(paket):
    # TCP ve Raw katmanı olan paketleri kontrol et
    if paket.haslayer(TCP) and paket.haslayer(Raw):
        payload = paket[Raw].load.decode(errors='ignore')
        if "HTTP" in payload or "GET" in payload or "POST" in payload:
            print(f"HTTP Paketi Yakalandı: {paket.summary()}")
            print(payload)
            print("-" * 80)

def main():
    print("HTTP paket yakalama başlatıldı... (Ctrl+C ile durdurabilirsiniz)")
    sniff(filter="tcp port 80", prn=paket_yakala, store=False)

if __name__ == "__main__":
    main()
