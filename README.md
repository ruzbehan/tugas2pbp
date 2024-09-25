Tautan Aplikasi PWS : https://pbp.cs.ui.ac.id/web/project/muhammad.ruzbehan/belisate


TUGAS 2

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
    Client akan mengirim request ke URL yang ditentukan di urls.py, yang diarahkan ke fungsi di views.py. 
    Jika diperlukan data dari database, view akan memanggil model di models.py, dan hasil akhirnya ditampilkan menggunakan template HTML.

    versi lengkap bagan sebagai berikut : 
    ``` 
    Permintaan (Request) dari Klien
                 ↓
    urls.py (Routing: Memetakan URL)
                 ↓
    views.py (Logika dan Pengambilan Data)
                 ↓
    models.py (Akses Database jika diperlukan)
                 ↓
    views.py (Mengembalikan Data ke View)
                 ↓
    Template HTML (Menampilkan Data dalam Halaman Web)
                 ↓
    Respon (Response) ke Klien (Halaman HTML)


Pertanyaan 3 : Jelaskan fungsi git dalam pengembangan perangkat lunak!

    Git adalah sistem version control yang digunakan untuk melacak perubahan kode sumber dalam pengembangan perangkat lunak. 
    Dengan Git, pengembang dapat bekerja sama / kolaboratif untuk melacak setiap perubahan dan memulihkan versi sebelumnya jika terjadi kesalahan.

Pertanyaan 4 : Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

    Menurut beberapa sumber yang saya dapatkan, django dipilih karena merupakan framework yang powerful, 
    namun tetap mudah dipahami oleh pemula. Django juga menyediakan banyak fitur built-in, seperti ORM, 
    autentikasi, dan routing, sehingga pengembang dapat fokus pada logika bisnis.

Pertanyaan 5 : Mengapa model pada Django disebut sebagai ORM?

    Model di Django disebut ORM (Object-Relational Mapping) karena ia berfungsi untuk memetakan objek di kode Python ke tabel di database secara otomatis. 
    ORM memungkinkan kita untuk berinteraksi dengan database menggunakan objek Python, tanpa harus menulis query SQL secara langsung.


TUGAS 3

Pertanyaan 1 : Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

    Data delivery memungkinkan pertukaran informasi antara client dan server. Tanpa mekanisme ini, aplikasi tidak dapat menyajikan konten dinamis, seperti produk atau informasi pengguna yang diambil dari database.

Pertanyaan 2 : Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

    JSON lebih populer karena:

       - Lebih ringan dan lebih mudah dibaca oleh manusia.
       - Memiliki struktur yang lebih sederhana dibandingkan XML.
       - JSON lebih mudah diintegrasikan dengan JavaScript, yang banyak digunakan di aplikasi web modern.

Pertanyaan 3 : Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut

    Method is_valid() memeriksa apakah data yang dimasukkan ke dalam form sesuai dengan validasi yang telah ditentukan. Jika valid, data tersebut dapat diproses lebih lanjut. Ini penting untuk mencegah data yang tidak valid masuk ke dalam sistem.

Pertanyaan 4 : Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada     form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

    csrf_token digunakan untuk mencegah Cross-Site Request Forgery (CSRF), yaitu jenis serangan yang memanfaatkan kepercayaan yang dimiliki sebuah situs terhadap pengguna yang sudah terautentikasi. Jika tidak ada csrf_token, penyerang dapat mengirimkan permintaan palsu yang terlihat real.

Pertanyaan 5 : Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    Saya akan membagi checklist tersebut dalam beberapa bagian yaitu: 

        1. Membuat input form untuk menambahkan objek model pada app sebelumnya.

            Pertama-tama kita harus membuat file baru bernama forms.py di folder aplikasi main, kemudian tambahkan form berdasarkan model yang dibutuhkan untuk aplikasi kita. Disini saya membeerikan model Product. Lalu buat class ProductForm dan menambahkan fields penting dalam product, berikut kode saya :

            ```python
            from django.forms import ModelForm
            from main.models import Product

            class ProductForm(ModelForm):
                class Meta:
                    model = Product
                    fields = ["name", "price", "description", "quantity"]
            ```       

        2.  Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.

            Seperti yang saya sebutkan sebelumnya, kita membuat form berdasarkan model Product di forms.py. Setelah itu, kita tambahkan form tersebut ke dalam views dan template untuk membuat halaman input produk.
            Berikut kode saya :

            ```python
            def show_xml(request):
                data = Product.objects.all()
                return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

            def show_json(request):
                data = Product.objects.all()
                return HttpResponse(serializers.serialize("json", data), content_type="application/json")

            def show_xml_by_id(request, id):
                data = Product.objects.filter(pk=id)
                return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

            def show_json_by_id(request, id):
                data = Product.objects.filter(pk=id)
                return HttpResponse(serializers.serialize("json", data), content_type="application/json")
            ```

        3. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2

            Routing masing-masing views dapat ditambahkan pada urls.py dengan menambahkan kode ini pada baguan urlpatterns

            ```python
            urlpatterns = [
            path('', show_main, name='show_main'),
            path('create-product', create_product, name='create_product'),
            path('xml/', show_xml, name='show_xml'),
            path('json/', show_json, name='show_json'),
            path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
            path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
            ]
            ```


TUGAS 4

Pertanyaan 1 : Apa perbedaan antara HttpResponseRedirect() dan redirect()?

        Redirect() merupakan shortcut yang digunakan di Django untuk melakukan hal yang sama seperti HttpResponseRedirect(), tetapi penulisan kode menjadi lebih rapih. Fungsi redirect() bisa menerima URL, nama view, atau bahkan objek model, dan secara otomatis 
        mengarahkan pengguna ke halaman yang sesuai. Perbedaan utama yaitu redirect() adalah shortcut untuk HttpResponseRedirect() yang lebih fleksibel dan memudahkan pemrograman, sementara HttpResponseRedirect() adalah cara manual untuk mengarahkan pengguna.

Pertanyaan 2 : Jelaskan cara kerja penghubungan model Product dengan User!

        Untuk menghubungkan model Product dengan User, kita perlu menggunakan relasi ForeignKey di model Product. Hal ini memungkinkan setiap entri produk terkait dengan pengguna tertentu (satu pengguna bisa memiliki banyak produk).

        ```python
        from django.db import models
        from django.contrib.auth.models import User

        class Product(models.Model):
            name = models.CharField(max_length=100)
            price = models.IntegerField()
            description = models.TextField()
            user = models.ForeignKey(User, on_delete=models.CASCADE)  # Menghubungkan Product dengan User
        ```
        ForeignKey(User, on_delete=models.CASCADE) yaitu setiap produk terkait dengan satu pengguna. Jika pengguna dihapus, semua produk yang terkait dengan pengguna tersebut juga dihapus.

Pertanyaan 3 : Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

        Authentication (Autentikasi) adalah proses untuk memastikan identitas seorang pengguna, biasanya dengan meminta kredensial seperti username dan password. Saat pengguna login, Django memverifikasi kredensial mereka dan, jika valid, pengguna diizinkan masuk ke sistem.

        Authorization (Otorisasi) adalah proses menentukan izin apa yang dimiliki pengguna setelah mereka terautentikasi. Hal ini menentukan akses mereka terhadap sistem, seperti halaman, atau hak dalam tindakan tertentu.

        Ketika pengguna login di Django:

        1. Authentication dilakukan dengan mencocokkan username dan password.
        2. Setelah berhasil login, Django mengatur session dan cookies untuk menyimpan status pengguna yang telah terautentikasi.
        3. Authorization kemudian menentukan apa yang bisa dilakukan pengguna di aplikasi berdasarkan peran mereka (misalnya, admin atau pengguna biasa).

Pertanyaan 4 : Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

        Setelah pengguna berhasil login, Django membuat sesi di server yang menyimpan informasi pengguna yang sedang aktif.
        Django juga menulis cookie ke browser pengguna yang berisi ID sesi, agar memungkinkan server untuk mengidentifikasi pengguna tersebut pada request berikutnya.
        
        Penggunaan lain dari cookies:

            1. Menyimpan preferensi pengguna seperti bahasa yang dipilih atau mode tampilan.
            2. Pelacakan aktivitas: Seperti item dalam keranjang belanja atau halaman yang terakhir dilihat.

        
        Namun tidak semua cookies aman. Jika tidak dienkripsi, cookie bisa disadap oleh pihak ketiga. Untuk itu, Django mendukung penggunaan secure cookies dan HTTPOnly cookies untuk meningkatkan keamanan.

            1. Secure cookies: Hanya dikirim melalui koneksi HTTPS.
            2. HTTPOnly cookies: Tidak dapat diakses melalui JavaScript, mengurangi risiko serangan XSS (Cross-Site Scripting).

Pertanyaan 5 :

        1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
            Kita harus menambahkan fuction register, login_user, logout_user pada views.py di direktori main

        2. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
            Untuk langkah ini saya menyalakan server dengan perintah python manage.py runserver, lalu membuka web buatan saya dan menambahkan akun pengguna menggunakan register, setelah itu saya add 3 product baru untuk masing-masing user.

        3. Menghubungkan model Product dengan User.
            Cara menghubungkan model product dengan user yaitu dengan menambahkan ForeignKey ke model Product yang terhubung ke model User, sehingga setiap produk terkait dengan pengguna yang membuatnya.

        4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
            Cara menampilkan detail pengguna yang sedang login (seperti username) menggunakan request.user di template.
            lalu gunakan cookie untuk menyimpan informasi seperti last login dan tampilkan di halaman utama.
