Tautan Aplikasi PWS : 

Pertanyaan 1 : Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    CP 1 :
        Membuat sebuah proyek Django baru, setelah menginstal virtual environment dengan perintah : `python -m venv env`, Didalam directori yang sama harus membuat berkas requirements.txt yang natinya berisi dependencies penting dalam aplikasi django. Lalu setelah selesai melalukan instalasi dengan perintah : `pip install -r requirements.txt`, kita dapat mulai membuat aplikasi django,hal ini dapat dilakukan dengan perintah : `django-admin startproject main` dan dengan posisi env menyala , pada cmd tempat direktori yang sama (yang berisi requirements.txt dan env).

    CP 2 :
        Membuat aplikasi dengan nama main pada proyek tersebut. Pada perintah `django-admin startproject main`, "main" disini adalah nama aplikasi kita.

    CP 3 :
        Melakukan routing pada proyek agar dapat menjalankan aplikasi main. Routing dapat dilakukan dengan cara menambahkan :

        ```python
        from django.contrib import admin
        from django.urls import path
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('main.urls')),
        ]
        ```
        Pada urls.py di luar main.

    CP 4 :
        Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
        name
        price
        description
        Pada bagian ini kita hanya perlu membuat model sesuai atribut yang diperlukan serta sesuai dengan tipe yang diminta :

        ```python
        from django.db import models
        class Product(models.Model):
            name = models.CharField(max_length=100)
            price = models.IntegerField()  
            description = models.TextField()
            quantity = models.IntegerField()  

            def __str__(self):
                return self.name
        ```
        Disini saya menambahkan atribut quantity sebagai atribut tambahan saja. 

    CP 5: 
        Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
        Fungsi pada views.py dapat ditulis sebagai berikut : 

        ```python
        from django.shortcuts import render
        def show_main(request):
            context = {
                'name' : 'Sate Pacil',
                'price': 15000,
                'description': 'SATE PALING ENAK SE UI?!!!',
                'quantity' : 5
            }

            return render(request, "main.html", context)
        ```
        Atribut yang kita isi pada context adalah atribut yang dibutuhkan pada model, fungsi render() pada Django digunakan untuk memproses permintaan (request) dari client dan mengembalikan respon berupa halaman HTML. "main.html" adalah nama template HTML yang akan dirender dan ditampilkan ke pengguna
    
    CP 6 :
        Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
        Routing pada aplikasi main dapat ditulis sebagai berikut : 
        
        ```python 
        from django.urls import path
        from main.views import show_main

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
        ]
        ```
        app_name adalah variable nama aplikasi django kita, penjelasannya kurang lebih sama dengan CP 5

    CP 7 : 
        Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet. 
        Sebelum di deploy pada pws, kita harus membuat akun pws terlebih dahulu, apabila sudah terdapat project kita di pws, baru dapat kita push dengan cara `git push pws main:master` dan jangan lupa mengubah ALLOWED_HOSTS pada settings.py. 

        Apabila terdapat kesalahan pada pws, kita dapat menarik kembali/ mengganti dengan pws yang baru dengan perintah : `git remote remove pws` seperti kasus yang saya alami sendiri. Lalu kita dapat push kembali

Pertanyaan 2 : Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

    Bagan : `Client -> URL (urls.py) -> View (views.py) -> Model (models.py) -> Template (HTML)`
    Client akan mengirim request ke URL yang ditentukan di urls.py, yang diarahkan ke fungsi di views.py. Jika diperlukan data dari database, view akan memanggil model di models.py, dan hasil akhirnya ditampilkan menggunakan template HTML.

Pertanyaan 3 : Jelaskan fungsi git dalam pengembangan perangkat lunak!

    Git adalah sistem version control yang digunakan untuk melacak perubahan kode sumber dalam pengembangan perangkat lunak. Dengan Git, pengembang dapat bekerja sama / kolaboratif untuk melacak setiap perubahan dan memulihkan versi sebelumnya jika terjadi kesalahan.

Pertanyaan 4 : Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

    Menurut beberapa sumber yang saya dapatkan, django dipilih karena merupakan framework yang powerful, namun tetap mudah dipahami oleh pemula. Django juga menyediakan banyak fitur built-in, seperti ORM, autentikasi, dan routing, sehingga pengembang dapat fokus pada logika bisnis.

Pertanyaan 5 : Mengapa model pada Django disebut sebagai ORM?

    Model di Django disebut ORM (Object-Relational Mapping) karena ia berfungsi untuk memetakan objek di kode Python ke tabel di database secara otomatis. ORM memungkinkan kita untuk berinteraksi dengan database menggunakan objek Python, tanpa harus menulis query SQL secara langsung.
