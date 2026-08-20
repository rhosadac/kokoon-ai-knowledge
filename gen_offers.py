#!/usr/bin/env python3
"""Generate offers.txt dari kokoonhotelsvillas.com/banyuwangi/offer/ -> WhatsApp-ready text.
Data dinamis: scrape tiap jalan, format, tulis ke offers.txt.
Jalankan via cron / n8n Execute Command. Tidak perlu LLM.
"""
import re, sys, subprocess, datetime
from urllib.request import Request, urlopen

BASE = "https://kokoonhotelsvillas.com/banyuwangi"
LIST = f"{BASE}/offer/"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# Offer accommodation yang mau diambil (slug -> label baris)
ACCOM = {
    "mid-year-escape-room-breakfast": "MID YEAR ESCAPE – Room Breakfast",
    "mid-year-escape-room-only": "MID YEAR ESCAPE – Room Only",
    "weekend-escape": "WEEKEND ESCAPE",
}

def get(url):
    req = Request(url, headers=UA)
    with urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "ignore")

def clean(t):
    return re.sub(r"<[^>]+>", "", t).replace("&#8211;", "–").replace("&#038;", "&").replace("&amp;", "&").strip()

def price_of(html):
    # pola di halaman: <b>Price</b> IDR 980.000,- nett  (dalam <li>)
    m = re.search(r"Price\s*</b>\s*IDR\s*([\d\.]+)", html, re.S)
    if not m:
        m = re.search(r"Price[^<]*?</strong>\s*IDR\s*([\d\.]+)", html, re.S)
    return m.group(1) if m else None

def period_of(html):
    # <li><i fa fa-calendar></i> Valid Date : 1 July ... </li>
    m = re.search(r"fa-calendar[^>]*></i>\s*([^<]+?)(?:\n|</li>|$)", html, re.S)
    if not m:
        m = re.search(r"Valid Date\s*:\s*([^<]+?)(?:\n|$)", html, re.S)
    if not m:
        m = re.search(r"Stay Period:\s*([^<]+)", html)
    return clean(m.group(1)) if m else ""

def benefit_of(html):
    # <li><i fa fa-money></i> <b>Price</b> IDR ... ; <li>1 night stay...</li>
    # ambil <li> yang mengandung kata kunci benefit (bukan yang berisi Price/calendar)
    out = []
    for li in re.findall(r"<li[^>]*>(.*?)</li>", html, re.S):
        c = clean(li)
        if not c:
            continue
        if "Price" in c or "fa-calendar" in li or "Valid Date" in c:
            continue
        if any(k in c for k in ("night stay", "Breakfast", "upgrade", "Pizza", "Starbucks", "Room Only", "sarapan")):
            out.append(c)
    return out[:2]

def main():
    list_html = get(LIST)
    lines = []
    lines.append("🎁 *Promo & Penawaran Spesial Kokoon Hotel Banyuwangi*")
    lines.append("")
    lines.append("*Paket Menginap (Accommodation)*")
    for slug, label in ACCOM.items():
        url = f"{BASE}/offers/{slug}/"
        try:
            h = get(url)
        except Exception as e:
            lines.append(f"• {label} – (gagal ambil: {e})")
            continue
        price = price_of(h)
        per = period_of(h)
        ben = benefit_of(h)
        if price:
            lines.append(f"• *{label}*")
            lines.append(f"  IDR {price},- nett / malam")
            if ben:
                lines.append(f"  {'; '.join(ben)}")
            if per:
                lines.append(f"  Periode: {per}")
        else:
            lines.append(f"• *{label}* – (harga tidak ditemukan)")
    lines.append("")
    lines.append("*Paket Wisata Alam (Leisure)*")
    lines.append("• Ijen Blue Fire 2D1N & Hiking to Ijen – Petualangan api biru eksklusif.")
    lines.append("• Tabuhan & Menjangan 2D1N – Eksplorasi bawah laut.")
    lines.append("• Eksplorasi Taman Nasional – Baluran, Alas Purwo, Hutan Djawatan, Pulau Merah.")
    lines.append("")
    lines.append("*F&B & Fasilitas Lainnya*")
    lines.append("• Coffee Break – Kopi & pastry.")
    lines.append("• Swimming Package & Gym Membership – Tamu luar.")
    lines.append("• Fun Game Outbound – Tim & gathering.")
    lines.append("")
    lines.append("Detail fasilitas & syarat: https://kokoonhotelsvillas.com/banyuwangi/offer/")
    lines.append("")
    lines.append(f"_generated: {datetime.date.today().isoformat()}_")

    out = "\n".join(lines)
    with open("/root/offers.txt", "w") as f:
        f.write(out)
    print(out)

if __name__ == "__main__":
    main()
