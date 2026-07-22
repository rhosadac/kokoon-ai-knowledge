# Panduan Inject Meta + OG + llms.txt ke Website Kokoon

## File yang perlu dipasang

| File | Tujuan | Cara pasang |
|---|---|---|
| `meta-og-inject.html` | Meta description, OG tags, Twitter Card | Paste ke WordPress `<head>` |
| `llms.txt` | AI discoverability (ChatGPT, Claude, Perplexity) | Upload ke root website |

---

## 1. Meta + Open Graph + Twitter Card

### Opsi A — Plugin (RECOMMENDED, paling mudah)

1. Install plugin **"Insert Headers and Footers"** (by WPCode) atau **"Header Footer Code Manager"**
2. Buka Settings > Insert Headers and Footers
3. Copy seluruh isi `meta-og-inject.html`
4. Paste di bagian **"Header"** (Scripts in Header)
5. Save

### Opsi B — Theme Editor (langsung)

1. WordPress Dashboard > Appearance > Theme File Editor
2. Buka file `header.php`
3. Cari tag `</head>`
4. Paste seluruh isi `meta-og-inject.html` SEBELUM `</head>`
5. Update File

### Opsi C — Elementor (jika pakai Elementor)

1. Elementor > Custom Code > Add New
2. Name: "Meta OG Tags"
3. Location: `<head>`
4. Priority: 1
5. Paste isi `meta-og-inject.html`
6. Publish

---

## 2. llms.txt

File `llms.txt` harus bisa diakses di: `https://kokoonhotelsvillas.com/llms.txt`

### Opsi A — FTP/File Manager (RECOMMENDED)

1. Login ke hosting cPanel / File Manager
2. Buka folder root website (biasanya `/public_html/`)
3. Upload file `llms.txt` ke folder root (sejajar dengan `wp-config.php`)
4. Verify: buka `https://kokoonhotelsvillas.com/llms.txt` di browser

### Opsi B — WordPress Page + Redirect

1. Buat page baru di WordPress dengan slug `llms-txt`
2. Paste isi llms.txt sebagai plain text
3. Tambahkan redirect rule di `.htaccess`:
   ```
   RewriteRule ^llms\.txt$ /llms-txt/ [L]
   ```

---

## 3. Verifikasi

Setelah dipasang, cek:

1. **Meta tags**: View page source (Ctrl+U) > cari "og:title" dan "twitter:card"
2. **OG preview**: https://developers.facebook.com/tools/debug/ > masukkan URL hotel
3. **Twitter preview**: https://cards-dev.twitter.com/validator > masukkan URL hotel
4. **llms.txt**: buka https://kokoonhotelsvillas.com/llms.txt langsung di browser
5. **Rich Results**: https://search.google.com/test/rich-results > masukkan URL hotel

---

## Catatan

- Semua inject ini **TIDAK mengubah tampilan website** sama sekali
- Total payload: ~5 KB (sangat ringan, tidak mempengaruhi page speed)
- OG tags membuat share link di WhatsApp/Facebook/Telegram tampil preview gambar + deskripsi
- llms.txt membuat AI bisa langsung membaca dan merekomendasikan hotel
