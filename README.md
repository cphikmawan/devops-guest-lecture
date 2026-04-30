# DevOps Guest Lecture
**"Life as a DevOps Engineer at CSG (IT Consultant) & Ajaib (Fintech)"**

Slide presentasi untuk sesi sharing DevOps — perbandingan pengalaman di dua perusahaan berbeda.

---

## Cara Pakai

### 1. Isi konten pemateri

Masing-masing pemateri edit file di folder `content/`:

| File | Untuk |
|------|-------|
| `content/speaker-csg.json` | Pemateri dari CSG |
| `content/speaker-ajaib.json` | Pemateri dari Ajaib |

Buka file JSON, isi semua field, simpan.

### 2. Generate slide

```bash
python3 generate.py
```

Output: `slides.html` — langsung bisa dibuka di browser.

### 3. Present

Buka `slides.html` di browser, tekan `F` untuk fullscreen.

| Tombol | Fungsi |
|--------|--------|
| `→` / `Space` | Slide berikutnya |
| `←` | Slide sebelumnya |
| `F` | Fullscreen |
| `Esc` | Overview / keluar fullscreen |
| `S` | Speaker notes |

---

## Struktur File

```
devops-guest-lecture/
├── content/
│   ├── speaker-csg.json        <- isi ini (pemateri CSG)
│   └── speaker-ajaib.json      <- isi ini (pemateri Ajaib)
├── slides.template.html        <- template slide (jangan diedit)
├── slides.html                 <- output generated (jangan diedit manual)
├── generate.py                 <- script generator
└── presentation-outline.md     <- panduan lengkap materi
```

---

## Alur Kerja

```
speaker-csg.json   ─┐
                     ├─ generate.py ──→ slides.html
speaker-ajaib.json ─┘
```

Setiap kali ada perubahan di content file, jalankan `python3 generate.py` lagi.

---

## Requirements

Python 3.7+ — tidak ada dependency eksternal.
