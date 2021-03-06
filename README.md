# [**UserScenario2Seq**](https://github.com/AgileRE-2021/UserScenario2Seq/)

<br />
<p align="center">
<img src="https://github.com/AgileRE-2021/UserScenario2Seq/blob/4f72023c75d1e1688cc0acb5576b60d3bad5f449/userscenario2seq/core/static/assets/images/logo-new.png">
</p>
<br />

[UserScenario2Seq](https://github.com/AgileRE-2021/UserScenario2Seq/) merupakan aplikasi berbasis website yang 
memiliki fungsi utama generate artefak **Sequence Diagram** dari **User Story Scenarios**.
Tujuan utama dari aplikasi ini adalah memberi kemudahan dalam transformasi artefak sehingga 
dapat mengurangi biaya dan waktu pengembangan.
>- **User Story Scenarios** merupakan artefak yang berisi alur interaksi pengguna dengan sistem. Pada UserScenario2Seq, artefak ini dipakai dalam format **Behat Cheat Sheet**.
>- **Sequence Diagram** merupakan diagram yang menjelaskan alur cara kerja sistem. Pada UserScenario2seq, sequence diagram hanya dapat dibuat dari tiga elemen yaitu aktor, objek *boundary*, dan objek *control*.

Merupakan repository project milik kelompok 2 kelas I1 matakuliah Pembangunan Perangkat Lunak Praktikum. Memiliki fungsi utama untuk melakukan transformasi dari User Story Scenario menjadi Sequence Diagram.

## Cara Instalasi
1. Buat direktori/folder untuk menyimpan aplikasi
   ```sh
   mkdir *nama direktori*  
   ```
2. Masuk kedalam direktori/folder tersebut
   ```
   cd *nama direktori*  
   ```
3. Lakukan _clone_ pada _repository_    
   ```
   git clone https://github.com/AgileRE-2021/UserScenario2Seq.git 
   ```
4. Masuk ke folder project UserScenario2Seq
   ```
   cd UserScenario2Seq 
   ```
5. Masuk ke folder userscenario2seq
   ```
   cd userscenario2seq
   ```
6. Lakukan instalasi modul-modul yang digunakan
    ```
    pip3 install -r requirements.txt 
    ```
7. Buat migrasi untuk membuat database
    ```
    python manage.py makemigrations  
    ```
    ```
    python manage.py migrate  
    ```
8. Jalankan aplikasi UserScenario2Seq
    ```
    python manage.py runserver  
    ```
9. Gunakan port yang tersedia untuk mulai menggunakan aplikasi
    ```
    Akses aplikasi web di browser http://127.0.0.1:8000/
    ```
## Cara Penggunaan
<h3>Membuat Akun</h3>
<ol>
  <li>Jika belum memiliki akun, buat akun terlebih dahulu dengan menekan tombol <b>Sign Up</b> pada halaman Sign In</li>
  <li>Pada halaman register, isi seluruh informasi yang diperlukan (username, email, password, password-check)</li>
  <li>Centang bagian <i>I agree with terms</i></li>
  <li>Tekan tombol <b>Sign Up</b></li>
</ol>
<h3>Sign In</h3>
<ol>
  <li>Pada halaman login, masukkan username dan password</li>
  <li>Centang bagian <b>Save credentials</b> jika ingin akun diingat (tidak perlu sign in selama tidak melakukan sign out)</li>
  <li>Tekan tombol <b>Sign In</b></li>
</ol>
<h3>Melihat Tutorial</h3>
<ol>
  <li>Setelah Sign In, Anda akan dialihkan ke halaman tutorial</li>
  <li>Terdapat tiga tutorial pada halaman tersebut</li>
  <li>Tutorial yang tersedia adalah membuat project, membuat fitur, serta generate sequence diagram</li>
</ol>
<h3>Membuat Project</h3>
<ol>
  <li>Tekan tombol <b>Create Project</b> pada side bar untuk masuk ke halaman pembuatan project</li>
  <li>Masukkan informasi yang dibutuhkan berupa nama project dan deskripsinya</li>
  <li>Tekan tombol <b>Submit</b> untuk menyimpan project</li>
</ol>
<h3>Membuat Feature</h3>
<ol>
  <li>Tekan tombol <b>List Project</b> pada side bar untuk masuk ke halaman List Project</li>
  <li>Pilih project yang ingin digunakan, kemudian klik tombol <b>Detail</b></li>
  <li>Pada halaman detail project, tekan tombol <b>Add Feature</b></li>
  <li>Anda akan dialihkan ke halaman pembuatan fitur</li>
  <li>Isi seluruh form sesuai format yang sudah ditentukan, tekan tombol <b>Submit</b> jika sudah selesai</li>
</ol>
<h3>Generate Sequence Diagram</h3>
<ol>
  <li>Tekan tombol <b>List Project</b> pada side bar untuk masuk ke halaman List Project</li>
  <li>Pilih project yang ingin digunakan, kemudian klik tombol <b>Detail</b></li>
  <li>Tekan tombol <b>Generate Sequence</b> pada fitur yang diinginkan</li>
  <li>Sebuah tab baru akan terbuka. Tab tersebut berisi sequence diagram hasil generate user story scenario</li>
</ol>

## Django Template
### Gradient Able Django

Open-source dashboard generated by AppSeed in **Django** Framework. [Gradient Able](https://appseed.us/admin-dashboards/django-gradient-able) Bootstrap 4 Free/Lite Admin Template is a complete solution for your dashboard creation. **Gradient Able** stands out from the crowd with an elegant look that combines soft gradient colors with well-suited typography and great cards and graphics. 

<br />

> Features

- UI-Ready app, SQLite Database, Django Native ORM
- Modular design, clean code-base
- Session-Based Authentication, Forms validation
- Deployment scripts: Docker, Gunicorn / Nginx
- Support via **Github** and [Discord](https://discord.gg/fZC6hup).

<br />

> Links

- [Gradient Able Django](https://appseed.us/admin-dashboards/django-gradient-able) - Product page
- [Gradient Able Django Demo](https://django-gradient-able.appseed-srv1.com/) - LIVE App
- [Gradient Able Django PRO](https://appseed.us/admin-dashboards/django-dashboard-gradient-pro) - the premium version: more page, components and LIVE Support
