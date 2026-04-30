# Life as a DevOps Engineer at CSG & Ajaib
## Outline Lengkap + Detail Materi Slide

**Topik:** Life as a DevOps Engineer at CSG (IT Consultant) & Ajaib (Fintech)  
**Purpose:** Sharing pengalaman DevOps + Perbandingan 2 perusahaan berbeda  
**Format:** 2 pembicara — Pemateri A (CSG) & Pemateri B (Ajaib)  
**Durasi estimasi:** 90–120 menit (incl. QnA/Quiz)

---

## STRUKTUR SLIDE (Total: ~35–40 slide)

---

## BAGIAN 0 — OPENING (3 slide)

### Slide 1 — Cover
```
Judul:   "Life as a DevOps Engineer"
Subtitle: "CSG (IT Consultant) vs Ajaib (Fintech)"
Visual:  Terminal prompt aesthetic / infrastruktur diagram minimalis
Konten:  Nama pemateri, posisi, logo perusahaan
```

### Slide 2 — Agenda
```
1. 👋 Perkenalan & Perjalanan Karir
2. 🏢 Daily Life: CSG vs Ajaib
3. 🛠️ Review Mini Project
4. ⚡ DevOps Dulu vs Sekarang (Era AI)
5. 🚀 Prospek Karir DevOps ke Depan
6. 🎯 Quiz / QnA
```

### Slide 3 — Disclaimer / Ice Breaker
```
"Ini bukan kuliah. Ini cerita."
- Pengalaman bersifat personal, bukan satu-satunya path
- Ada banyak jalan menuju DevOps
- Ask anything, no stupid questions
```

---

## BAGIAN 1 — PERJALANAN KARIR (6 slide)

### Slide 4 — Timeline: Pemateri A (CSG)
```
[PEMATERI A ISI SENDIRI]
Format: Timeline horizontal
Titik-titik:
  - Kuliah jurusan: ____
  - First internship / project pertama: ____
  - Mulai kenal DevOps: ____
  - Bergabung CSG: ____
  - Role saat ini: ____
Key moment: "Aha moment pertama kali deploy ke production"
```

### Slide 5 — Timeline: Pemateri B (Ajaib)
```
[PEMATERI B ISI SENDIRI]
Format: Timeline horizontal
Titik-titik:
  - Kuliah jurusan: ____
  - First internship / project pertama: ____
  - Mulai kenal DevOps: ____
  - Bergabung Ajaib: ____
  - Role saat ini: ____
Key moment: "Moment paling chaos yang pernah dialami di prod"
```

### Slide 6 — "Apa yang Dimaksud DevOps?"
```
Bukan hanya tools — ini adalah CULTURE
┌─────────────────────────────────────────┐
│  Dev ←→ Ops : kolaborasi, bukan musuhan │
│  Build → Test → Deploy → Monitor → Fix  │
└─────────────────────────────────────────┘

3 pilar utama:
  1. Culture (komunikasi, shared responsibility)
  2. Automation (CI/CD, IaC, CaC)
  3. Measurement (observability, SLO/SLA)
```

### Slide 7 — Skill Map DevOps (Overview)
```
Visualisasi: Mind map atau hexagonal diagram
Cluster utama:
  - OS & Networking (Linux, TCP/IP, DNS)
  - Containers (Docker, Kubernetes)
  - IaC (Terraform, Pulumi)
  - CI/CD (Jenkins, GitHub Actions, GitLab CI)
  - Cloud (AWS/GCP/Azure)
  - Monitoring (Prometheus, Grafana, ELK)
  - Security (DevSecOps, SAST/DAST, Vault)
Catatan: Tidak perlu kuasai semua sekaligus
```

### Slide 8 — Realita vs Ekspektasi Kuliah
```
❌ Ekspektasi:          ✅ Realita:
Semua teori terpakai    80% learning on the job
Langsung jadi senior    3–6 bulan baru "ngerti flow"
Tools = skill           Problem-solving > tool knowledge
Sertifikasi = garansi   Portfolio > sertifikat

"Yang bikin kamu diterima: kemampuan belajar, bukan IPK"
```

### Slide 9 — Tips Masuk Dunia DevOps (dari pengalaman)
```
✅ DO:
  - Bangun home lab (VM, Docker, free-tier cloud)
  - Kontribusi open source / GitHub aktif
  - Ikuti komunitas (CNCF, DevOps Indonesia)
  - Tulis blog / dokumentasikan learnings

❌ AVOID:
  - Tutorial hell (tanpa praktek langsung)
  - Hanya koleksi sertifikat tanpa project nyata
  - Takut breaking things di lab
```

---

## BAGIAN 2 — DAILY LIFE: CSG vs AJAIB (8 slide)

### Slide 10 — Company Profile: CSG
```
[PEMATERI A ISI SENDIRI]
Kategori:   IT Consultant
Client:     Multi-client (list beberapa jika bisa)
Tim DevOps: Ukuran tim, struktur
Stack:      Tools/cloud yang digunakan
Culture:    Pace kerja, WFH/WFO, on-call?
```

### Slide 11 — Company Profile: Ajaib
```
[PEMATERI B ISI SENDIRI]
Kategori:   Fintech (investment platform)
Scale:      Jumlah user / transaksi (umum)
Tim DevOps: Ukuran tim, struktur
Stack:      Tools/cloud yang digunakan
Culture:    Pace kerja, WFH/WFO, on-call?
```

### Slide 12 — Daily Task: CSG (IT Consultant)
```
[PEMATERI A ISI SENDIRI — template di bawah]

Typical Monday–Friday:
  Morning:  Stand-up, cek alert/monitoring
  Day:      [isi aktivitas utama]
  Afternoon: [isi aktivitas]

Tugas rutin:
  □ Infrastructure provisioning untuk client
  □ Manage multiple environment (dev/staging/prod)
  □ On-call rotation
  □ Client meeting / technical alignment

Tugas ad-hoc:
  □ Incident response
  □ Cost optimization
  □ Security audit
```

### Slide 13 — Daily Task: Ajaib (Fintech)
```
[PEMATERI B ISI SENDIRI — template di bawah]

Typical Monday–Friday:
  Morning:  Stand-up, cek dashboard metrik transaksi
  Day:      [isi aktivitas utama]
  Afternoon: [isi aktivitas]

Tugas rutin:
  □ Deploy & release management (microservices)
  □ Monitor SLA/SLO untuk financial transaction
  □ Database reliability & backup
  □ Compliance & audit readiness (OJK/BI)

Tugas ad-hoc:
  □ Incident response (high severity = P1)
  □ Capacity planning jelang market event
  □ Security patching
```

### Slide 14 — Scope & Responsibility Comparison
```
                  CSG (Consultant)     Ajaib (Fintech)
─────────────────────────────────────────────────────
Jumlah client:    Multi-client         Single product
Scope:            Broad, varied        Deep, focused
On-call:          Tergantung kontrak   24/7 (financial)
Regulasi:         Per-client           OJK/BI compliance
Scale infra:      Per-project          High-scale (prod)
Learning speed:   Cepat (diverse)      Mendalam (domain)
Tech ownership:   Client-driven        Internal ownership
```

### Slide 15 — Tantangan Unik di CSG
```
[PEMATERI A ISI SENDIRI]
Contoh challenge nyata:
  1. Multi-client multi-stack: manage context switch
  2. Legacy system client yang butuh modernisasi
  3. Timeline project yang ketat
  4. Security requirement berbeda per client

"Cerita satu insiden menarik (anonim)"
```

### Slide 16 — Tantangan Unik di Ajaib
```
[PEMATERI B ISI SENDIRI]
Contoh challenge nyata:
  1. Zero downtime saat market open (09.00–15.30)
  2. Database consistency untuk transaksi finansial
  3. Regulasi OJK = setiap deployment harus documented
  4. Flash-scale saat event promo / IPO besar

"Cerita satu insiden menarik (anonim)"
```

### Slide 17 — Gaji & Jenjang Karir (Realita)
```
Level DevOps Engineer (rough range, 2024–2025):

Junior (0–2 thn):     Rp 6–12 juta/bulan
Mid (2–4 thn):        Rp 12–22 juta/bulan
Senior (4–7 thn):     Rp 22–40 juta/bulan
Staff/Principal:      Rp 40–70 juta/bulan

Faktor yang berpengaruh:
  ✅ Cloud certification (AWS/GCP/CKA)
  ✅ Company stage (startup vs enterprise)
  ✅ Domain (fintech premium vs non-fintech)
  ✅ English proficiency (untuk perusahaan global)

Sumber: Glassdoor, LinkedIn Salary, komunitas
```

---

## BAGIAN 3 — REVIEW MINI PROJECT (8 slide)

### Slide 18 — Overview 4 Studi Kasus
```
┌──────────────────────────────────────────────────────┐
│  #1  High Availability Load Balancer (Tiket Konser)  │
│  #2  HA Database + ProxySQL (E-Commerce)             │
│  #3  CI/CD Pipeline + DevSecOps (Tim Dev)            │
│  #4  Observability Stack (Prometheus + Grafana)      │
└──────────────────────────────────────────────────────┘
Benang merah:
  Docker → Terraform → Ansible = IaC + CaC + Containers
  Semuanya relevan dengan pekerjaan nyata di industri
```

### Slide 19 — Studi Kasus #1: HA Load Balancer
```
Konteks: Server down saat war tiket konser
Arsitektur:  1 LB + 4 Workers (2 FE + 2 BE)
Yang dikerjakan:
  □ Docker: Containerize FE + BE + security scan
  □ Terraform: Provision di Azure (VMs, network)
  □ Ansible: Install Docker, setup Nginx/HAProxy
Nilai tambah: Load testing k6 (1.000 concurrent users)

🔴 Di dunia nyata (CSG/Ajaib):
  "Kalau ini production Ajaib saat stock rush —
   downtime = miliaran rupiah, dan OJK bisa teguran"
  
  CSG: "Kami pernah handle event serupa untuk klien
       e-commerce, dan perbedaannya adalah..."
```

### Slide 20 — Studi Kasus #2: HA Database + ProxySQL
```
Konteks: E-commerce DB single point of failure
Arsitektur:  ProxySQL + 1 Master + 2 Slave + App Node
Yang dikerjakan:
  □ Docker: App + ProxySQL images + security scan
  □ Terraform: 5 VMs di Azure + isolated network
  □ Ansible: MySQL replication, SSL/TLS, backup cron
Nilai tambah: Health check otomatis + zero-downtime patching

🔴 Di dunia nyata:
  Fintech (Ajaib): "Database replication adalah KRITIS
   — setiap transaksi harus consistent, tidak boleh lost"
  Pola yang sama dipakai untuk PostgreSQL/Aurora di production
```

### Slide 21 — Studi Kasus #3: CI/CD Pipeline + DevSecOps
```
Konteks: Rilis manual = lambat, inconsistent, insecure
Arsitektur:  Jenkins + GitHub + Docker Hub + Deploy Node
Yang dikerjakan:
  □ Docker: Build image, security scan (docker scout)
  □ Terraform: 2 VMs (Jenkins + Deploy target)
  □ Ansible: Install deps, JCasC, deployment script
  □ Jenkinsfile: Pipeline as Code
Nilai tambah: Traceability commit→release, rollback auto, notifikasi

🔴 Di dunia nyata:
  "Di Ajaib: pipeline kami jalankan ~50–100 deploy/minggu
   tanpa pipeline yang solid, chaos bisa terjadi"
  "Di CSG: tiap client beda tools — GitHub Actions, 
   GitLab CI, Jenkins — adaptasi adalah kuncinya"
```

### Slide 22 — Studi Kasus #4: Observability Stack
```
Konteks: Tidak bisa deteksi masalah performa sebelum launch
Arsitektur:  App Node + Monitoring (Prometheus+Grafana) + k6
Yang dikerjakan:
  □ Docker Compose: Full monitoring stack
  □ Terraform: 2 VMs + network rules untuk scraping
  □ Ansible: Deploy app, exporter, seed dashboard Grafana
  □ k6 script: 1.000 VUs, 5 menit, p95 < 200ms
Nilai tambah: Alertmanager, performance traceability

🔴 Di dunia nyata:
  "Golden signal: Latency, Traffic, Errors, Saturation (LETS)
   Kalau keempat ini dimonitor, kamu bisa tidur lebih nyenyak"
  "Ajaib punya >200 dashboard Grafana untuk berbagai service"
```

### Slide 23 — Mapping Project ke Real World Tools
```
Mini Project → Production Equivalent

Docker Scout       → Trivy, Snyk, Prisma Cloud
Nginx/HAProxy      → AWS ALB, GCP Load Balancer, Envoy
Terraform (Azure)  → Terragrunt, Atlantis (GitOps IaC)
Ansible Playbook   → Chef, Puppet, SaltStack (enterprise)
Jenkins            → GitHub Actions, GitLab CI, ArgoCD
ProxySQL           → AWS RDS Proxy, PgBouncer
Prometheus+Grafana → Datadog, New Relic, Elastic APM
k6                 → Gatling, Locust, Artillery

💡 Prinsip sama, tools bisa beda — fokus pada konsep
```

### Slide 24 — Saran untuk Mini Project
```
Dari perspektif reviewer industri:

✅ Yang bikin nilai tinggi:
  1. README yang jelas: "setup 5 menit, bukan 5 jam"
  2. Clean code Terraform — gunakan modules + variables
  3. Ansible role yang reusable, bukan spaghetti playbook
  4. Security scan hasilnya di-address (bukan di-ignore)
  5. Video demo yang terstruktur (cerita, bukan asal demo)

❌ Yang sering menyebabkan gagal:
  - Hardcode credentials di repository
  - Terraform state disimpan locally (harusnya remote)
  - Tidak ada dokumentasi arsitektur
  - Pipeline yang tidak pernah gagal (berarti tidak ada test)
```

### Slide 25 — "Apa yang Tidak Diajarkan di Kampus"
```
Mini project mengajarkan teknis. Industri butuh ini juga:

🔐 Security mindset:
   Jangan commit .env, gunakan secret manager (Vault/SSM)

📊 Cost awareness:
   Setiap VM yang jalan = uang. Destroy resource kalau tidak pakai.

📝 Documentation as code:
   Kalau tidak terdokumentasi, seolah tidak pernah ada

🤝 Communication:
   DevOps adalah jembatan Dev–Ops–Business
   
⏰ Post-mortem culture:
   Insiden bukan aib, tapi kesempatan belajar
```

---

## BAGIAN 4 — DEVOPS DULU VS SEKARANG (5 slide)

### Slide 26 — Evolusi DevOps (Timeline)
```
2009  DevOps lahir (Flickr "10 deploys a day")
2013  Docker merevolusi containerization
2015  Kubernetes → container orchestration era
2018  GitOps / IaC menjadi mainstream
2020  Platform Engineering mulai tumbuh
2022  ChatGPT & AI coding assistant masuk industri
2023  AI-assisted DevOps, Copilot di pipeline
2024  AI Agents mulai automate toil tasks
2025  Platform Engineering + AI = Developer Self-Service

Tren: Makin abstrak, makin otomatis, makin cepat
```

### Slide 27 — Sebelum vs Sesudah AI dalam DevOps
```
DULU (Pre-2022):                SEKARANG (AI Era):
─────────────────────────────────────────────────
Tulis Terraform manual       → GitHub Copilot suggest IaC
Google Stack Overflow        → Tanya Claude/GPT langsung
Debugging manual log         → AI log analysis (Datadog AI)
Onboarding 3–6 bulan         → AI-assisted → 1–2 bulan
Script bash tulis dari nol   → AI generate + review
Runbook = dokumen statis      → AI-generated runbook otomatis
Alert = manusia analisa       → AIOps auto-correlate + suggest fix

"AI tidak menggantikan DevOps engineer.
 AI menggantikan DevOps engineer yang tidak pakai AI."
```

### Slide 28 — AI Tools yang Dipakai Sekarang
```
Kategori          Tools                  Fungsi
──────────────────────────────────────────────────────
Coding Assistant  GitHub Copilot         Autocomplete IaC/script
                  Cursor, Claude Code    Refactor, explain code
                  
Log Analysis      Datadog Watchdog       Anomaly detection
                  Elastic AI             Root cause analysis

IaC Generation    Claude, Copilot Chat   Generate Terraform
                  Pulumi AI              Natural language → IaC

Incident          PagerDuty AI           Alert correlation
Management        FireHydrant AI         Auto-runbook suggestion

Security          Snyk AI                Vuln fix suggestion
                  AWS Inspector AI       Prioritize findings

Testing           k6 AI (Grafana)        Script generation
```

### Slide 29 — Platform Engineering: The Next Wave
```
Trend besar 2024–2025: Internal Developer Platform (IDP)

Sebelum:  Developer → buka tiket ke DevOps → tunggu 2 hari
Sekarang: Developer → self-service portal → deploy sendiri

Komponen IDP:
  ┌─────────────────────────────────────────────┐
  │  Service Catalog   │  Backstage by Spotify   │
  │  CI/CD Template    │  GitHub Actions template│
  │  Cloud Resources   │  Terraform + Atlantis   │
  │  Secrets Manager   │  Vault / AWS SSM        │
  │  Observability     │  Grafana + Prometheus   │
  └─────────────────────────────────────────────┘

DevOps → Platform Engineer:
  "Kamu tidak lagi deploy untuk developer
   Kamu build platform yang developer pakai sendiri"
```

### Slide 30 — DevOps vs SRE vs Platform Engineer
```
                DevOps Eng    SRE          Platform Eng
────────────────────────────────────────────────────────
Focus          Delivery       Reliability  Developer UX
Primary goal   Ship faster    Stay stable  Self-service
Owns           Pipeline       SLO/SLA/Error Budget  IDP
Coding level   Medium         High (SWE bg) High
On-call        Yes            Yes (primary) Sometimes
Mindset        Collaboration  Error budget  Product thinking

"Di Indonesia kebanyakan masih 'DevOps' yang gabungan semua.
 Makin mature perusahaannya, makin spesifik role-nya."
```

---

## BAGIAN 5 — PROSPEK KARIR (4 slide)

### Slide 31 — Job Market DevOps 2025
```
Data (LinkedIn Indonesia, 2024–2025):
  - DevOps/Cloud Engineer: top 5 IT job demand
  - Skill paling dicari: Kubernetes, Terraform, AWS/GCP
  - Perusahaan yang paling banyak hire: Bank digital, Fintech, E-commerce

Global context:
  - DevOps Engineer median salary (US): $130,000/yr
  - Cloud market CAGR: ~17% per tahun hingga 2030
  - AI & automation mendorong demand Platform Engineer

Indonesia-specific:
  - Fintech boom → banyak butuh SRE/DevOps compliance-aware
  - Bank BUMN digital transformasi → butuh DevOps massif
  - Startup ecosystem tetap tumbuh (walau lebih selective)
```

### Slide 32 — Jalur Karir DevOps
```
Entry Point beragam:

Sysadmin → DevOps → SRE → Principal SRE
Developer → DevOps → Platform Engineer → Staff Eng
Network Eng → Cloud Eng → Cloud Architect
Security → DevSecOps → Cloud Security Architect

Sertifikasi yang valuable (2025):
  ⭐ CKA/CKAD (Kubernetes)          = global standard
  ⭐ AWS Solutions Architect         = paling banyak dicari
  ⭐ HashiCorp Terraform Associate   = IaC credential
  ★  GCP Professional DevOps         = growing demand
  ★  RHCE/RHCSA                      = enterprise Linux
```

### Slide 33 — "Will AI Replace DevOps Engineers?"
```
Jujur: Ya, sebagian pekerjaan akan hilang.
       Tapi bukan kamu kalau kamu adapt.

Yang akan ter-automate:
  ❌ Menulis boilerplate Terraform
  ❌ Copy-paste alert dari runbook
  ❌ Basic ticket resolution (L1 ops)
  ❌ Writing deployment scripts from scratch

Yang tetap butuh manusia:
  ✅ Architecture decision + trade-off analysis
  ✅ Incident commander saat chaos
  ✅ Stakeholder communication (business impact)
  ✅ Security judgment (AI suggests, human decides)
  ✅ Building culture + processes
  ✅ Context-aware debugging (knowing what matters)

"AI adalah junior engineer kamu yang tidak pernah lelah.
 Kamu adalah senior yang mengarahkan."
```

### Slide 34 — Saran untuk Mahasiswa yang Mau Mulai
```
Roadmap 12 bulan pertama:

Bulan 1–3 (Foundation):
  □ Linux proficient: file system, process, network
  □ Git mastery: branching, merge, rebase
  □ Docker: build image, docker-compose, registry

Bulan 4–6 (Cloud & IaC):
  □ Pilih 1 cloud (AWS free tier atau Azure student)
  □ Terraform: deploy simple infra
  □ CI/CD: GitHub Actions pipeline sederhana

Bulan 7–9 (Intermediate):
  □ Kubernetes basics (minikube/k3s)
  □ Monitoring: Prometheus + Grafana
  □ Ansible untuk konfigurasi otomatis

Bulan 10–12 (Portfolio):
  □ Build 1–2 project end-to-end (seperti mini project ini!)
  □ Dokumentasikan di GitHub
  □ Tulis 2–3 blog post di Medium/dev.to
  □ Apply internship / junior position
```

---

## BAGIAN 6 — QUIZ / QnA (2 slide)

### Slide 35 — Quiz Interaktif (5 Soal)
```
Format: Kahoot / Mentimeter / raise hand

Q1 (Mudah): Apa kepanjangan dari CI/CD?
   A) Continue Integration / Continuous Deployment ✅
   B) Code Integration / Code Deployment
   C) Container Infrastructure / Cloud Delivery

Q2 (Mudah): Tool mana yang digunakan untuk IaC?
   A) Ansible   B) Terraform ✅   C) Jenkins   D) k6

Q3 (Sedang): Apa fungsi ProxySQL dalam arsitektur database?
   A) Backup otomatis
   B) Query router read/write splitting ✅
   C) Enkripsi database
   D) Monitoring query slow log

Q4 (Sedang): Apa itu "Golden Signals" dalam monitoring?
   A) CPU, RAM, Disk, Network
   B) Latency, Traffic, Errors, Saturation ✅
   C) Uptime, MTTR, MTBF, Throughput

Q5 (Sulit): Apa perbedaan utama SRE vs DevOps Engineer?
   [Open discussion — tidak ada jawaban tunggal]
   Hint: Error budget, SLO, toil reduction
```

### Slide 36 — QnA + Penutup
```
"3 hal yang semoga kalian bawa pulang hari ini:"

1. DevOps bukan hanya tools — ini mindset
2. Learning never stops, tapi mulai dari sekarang
3. AI adalah multiplier, bukan pengganti

Kontak pemateri:
  Pemateri A (CSG):    LinkedIn: [isi]  Email: [isi]
  Pemateri B (Ajaib):  LinkedIn: [isi]  Email: [isi]

"Kalau stuck, DM kami. Kita komunitas, bukan kompetisi."
```

---

## APPENDIX — TOOLS & CARA BUAT SLIDE

---

## REKOMENDASI TOOLS UNTUK SLIDE

### Opsi 1: Gamma.app (PALING DIREKOMENDASIKAN untuk automation)
```
URL: https://gamma.app
Cara kerja: Input teks/outline → AI generate slide otomatis
Kelebihan:
  ✅ Tempel outline ini → 30 menit jadi slide lengkap
  ✅ Template modern & profesional
  ✅ Bisa export ke PDF atau present langsung
  ✅ Free tier cukup untuk 1 presentasi
Langkah:
  1. Buka gamma.app → "New AI"
  2. Paste outline bagian per bagian
  3. Pilih tema/warna (rekomendasi: dark tech theme)
  4. Review + edit manual untuk personal detail
```

### Opsi 2: Canva (Populer, mudah kolaborasi)
```
URL: https://canva.com
Kelebihan:
  ✅ Template presentasi tech yang bagus
  ✅ Kolaborasi real-time (2 pemateri bisa edit bareng)
  ✅ Magic Design: describe → auto-generate layout
  ✅ Export ke PPT/PDF/PNG
Template yang cocok:
  Search: "tech presentation" atau "DevOps" di Canva
  Style: Dark background + accent warna biru/hijau/oranye
```

### Opsi 3: Marp (Developer-friendly, Markdown → Slide)
```
Tool: Marp (https://marp.app) atau VS Code extension Marp
Format: Markdown file → PDF/HTML slide
Kelebihan:
  ✅ Version control dengan Git (slide as code)
  ✅ Cocok untuk developer
  ✅ Otomasi via CLI: marp outline.md --pdf

Contoh syntax Marp:
---
marp: true
theme: default
---
# Judul Slide
Konten slide

---
# Slide berikutnya
```

### Opsi 4: Google Slides + Claude
```
Workflow:
  1. Buka Google Slides
  2. Pilih template "Spearmint" atau "Coral" (clean + modern)
  3. Tempel konten dari file ini per slide
  4. Gunakan Claude untuk: generate visual metaphors,
     suggest better wording, create table/diagram content

Collaboration:
  Share link → 2 pemateri isi bagian masing-masing
  Gunakan komentar untuk alignment sebelum present
```

---

## DESIGN GUIDE UNTUK SLIDE

### Color Palette (Tech/DevOps theme)
```
Background:  #0D1117 (GitHub dark) atau #1A1B26 (Tokyo Night)
Primary:     #58A6FF (electric blue)
Secondary:   #3FB950 (terminal green)
Accent:      #FF7B72 (error red / warning)
Text:        #E6EDF3 (off-white)
Subtle:      #8B949E (secondary text)
```

### Typography
```
Header font:   JetBrains Mono / Fira Code (monospace = tech feel)
Body font:     Inter / Roboto (readable)
Code blocks:   JetBrains Mono, size 14–16
```

### Prinsip Desain
```
1. 1 slide = 1 ide utama
2. Max 6 bullet points per slide
3. Lebih banyak visual (diagram, icon) daripada teks panjang
4. Gunakan icon dari Flaticon/Lucide yang relevan
5. Setiap section punya warna header yang konsisten
6. Slide kode gunakan syntax highlighting (dark theme)
```

### Struktur Visual per Section
```
Bagian 0 (Opening):    Bold title + visual background
Bagian 1 (Perjalanan): Timeline horizontal
Bagian 2 (Daily Life): Table comparison / split layout
Bagian 3 (Project):    Architecture diagram + checklist
Bagian 4 (Era AI):     Before/After comparison
Bagian 5 (Prospek):    Roadmap + stats visual
Bagian 6 (Quiz):       Big bold Q&A format
```

---

## WORKFLOW OTOMASI DENGAN AI

### Option A: Gamma.app (Termudah)
```
Step 1: Copy section per section dari file ini
Step 2: Buka gamma.app → New → Paste + Generate
Step 3: Fine-tune layout, tambah logo perusahaan
Step 4: Share link ke co-speaker untuk isi bagian mereka
Estimasi waktu: 1–2 jam
```

### Option B: Claude + Canva
```
Step 1: Buka Claude, paste outline ini
Step 2: Minta Claude generate visual metaphor / icon suggestion
        Prompt: "Untuk slide tentang CI/CD pipeline,
                 suggest 3 visual metaphor yang relatable
                 untuk mahasiswa teknik"
Step 3: Buka Canva, tempel konten, gunakan saran visual
Step 4: Export PDF untuk backup, share link untuk live present
Estimasi waktu: 2–3 jam
```

### Option C: Marp + GitHub (For DevOps pride)
```
Step 1: Buat repo GitHub: "devops-guest-lecture"
Step 2: Buat file presentation.md dengan syntax Marp
Step 3: Install Marp CLI: npm install -g @marp-team/marp-cli
Step 4: Generate: marp presentation.md --html --output index.html
Step 5: Deploy ke GitHub Pages → link bisa dibagikan
Bonus: Version controlled, bisa PR untuk revisi!
Estimasi waktu: 3–4 jam (tapi keren banget buat portfolio)
```

---

## CHECKLIST PERSIAPAN

### 1 Minggu Sebelum
```
[ ] Pemateri A isi bagian CSG (slide 4, 10, 12, 15)
[ ] Pemateri B isi bagian Ajaib (slide 5, 11, 13, 16)
[ ] Pilih dan setup slide tool
[ ] Generate slide dari outline ini
[ ] Review bersama: timing + konten
[ ] Siapkan demo singkat jika ada (terminal, dashboard)
```

### 1 Hari Sebelum
```
[ ] Final review slide
[ ] Cek koneksi internet venue
[ ] Siapkan backup PDF (kalau koneksi bermasalah)
[ ] Brief tentang audience (semester berapa, background)
[ ] Siapkan soal quiz di Kahoot/Mentimeter
[ ] Konfirmasi durasi total (90 menit? 120 menit?)
```

### Hari H
```
[ ] Datang 30 menit lebih awal
[ ] Test proyektor, audio, koneksi
[ ] Buka slide di 2 device (backup)
[ ] Siapkan air minum 😄
[ ] Remember: Ini sharing, bukan sidang skripsi. Be chill.
```

---

## ESTIMASI TIMING

```
Bagian              Slide   Durasi
─────────────────────────────────
Opening             3       5 menit
Perjalanan Karir    6       20 menit (10 menit per pemateri)
Daily Life          8       20 menit (10 menit per pemateri)
Review Mini Project 8       25 menit
DevOps Era AI       5       15 menit
Prospek Karir       4       10 menit
Quiz / QnA          2       20 menit
─────────────────────────────────
TOTAL               36      ~115 menit (~2 jam)

Fleksibel: Potong bagian "Prospek" jadi 5 menit
           kalau waktu lebih singkat → total ~110 menit
```

---

*File ini dibuat: 2026-04-30*  
*Working dir: /Users/cloudy/Work/experiment/kuliah-tamu/*
