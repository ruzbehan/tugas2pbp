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
        redirect(): Merupakan shortcut yang digunakan di Django untuk melakukan hal yang sama seperti HttpResponseRedirect(), tetapi penulisan kode menjadi lebih rapih. Fungsi redirect() bisa menerima URL, nama view, atau bahkan objek model, dan secara otomatis mengarahkan pengguna ke halaman yang sesuai. Perbedaan utama yaitu redirect() adalah shortcut untuk HttpResponseRedirect() yang lebih fleksibel dan memudahkan pemrograman, sementara HttpResponseRedirect() adalah cara manual untuk mengarahkan pengguna.

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

TUGAS 5

Pertanyaan 1: Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

    Dalam CSS, ketika beberapa selector diterapkan pada elemen yang sama, urutan prioritas (specificity) yang menentukan gaya mana yang akan digunakan adalah sebagai berikut (dari yang paling rendah hingga paling tinggi):

    1. Element Selector yaitu menargetkan elemen HTML secara langsung, misalnya div, p, span. Ini memiliki   prioritas yang paling rendah.

    2. Class Selector yaitu selector yang menggunakan tanda titik (.) untuk menargetkan elemen berdasarkan kelas, misalnya .container. Class lebih spesifik daripada element selector.

    3. ID Selector yaitu selector yang menggunakan tanda pagar (#) untuk menargetkan elemen berdasarkan ID, misalnya #header. ID lebih spesifik daripada class.

    4. Inline Styles yaitu gaya yang diterapkan langsung pada elemen HTML menggunakan atribut style="", misalnya <div style="color: red;">. Ini memiliki prioritas lebih tinggi dari selector biasa.

    5. Important Rule (!important) yaitu gaya yang ditandai dengan !important akan selalu diutamakan di atas selector lainnya, meskipun selector lain memiliki prioritas lebih tinggi.

    contoh : 
        ```css
        <p id="text" class="info" style="color: green;">Hello World!</p>
        ```
        Selector #text (ID) akan memiliki prioritas lebih tinggi dibanding .info (class).
        Namun, jika ada style="color: green;" di dalam tag <p>, gaya inline ini akan diterapkan.
        Jika color: red !important; diterapkan dalam CSS, maka gaya ini akan selalu diutamakan.

Pertanyaan 2 : Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

    Responsive Design adalah konsep dalam pengembangan web yang bertujuan untuk membuat tampilan dan fungsionalitas aplikasi web menyesuaikan dengan berbagai ukuran layar dan perangkat (misalnya, smartphone, tablet, desktop). Desain responsif penting karena semakin banyak pengguna yang mengakses aplikasi web melalui perangkat dengan ukuran layar yang berbeda.

    Contoh aplikasi :
        1. Aplikasi yang sudah menerapkan Responsive Design yaitu aplikasi seperti Twitter atau Facebook yang memiliki tampilan yang responsif dan konsisten di berbagai perangkat.

        2. Aplikasi yang belum menerapkan Responsive Design yaitu seperti situs web lama atau aplikasi lawas yang tidak dirancang dengan responsivitas, misalnya situs web buatan tahun 2000-an yang hanya berfungsi baik di desktop.

Pertanyaan 3 : Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

        1. Margin yaitu ruang di luar elemen. Margin mengatur jarak antara elemen tersebut dengan elemen lain di sekitarnya.

        Contoh: margin: 10px; memberi jarak 10px di luar elemen.

        Border yaitu garis yang mengelilingi elemen. Border ada di antara margin dan padding, dan dapat diatur ketebalan, warna, dan jenisnya.

        Contoh: border: 2px solid black; membuat border hitam dengan ketebalan 2px.

        Padding yaitu ruang di dalam elemen, antara konten dan border elemen. Padding menambah jarak di dalam elemen itu sendiri.
        
        Contoh: padding: 20px; menambah jarak 20px di dalam elemen, sebelum konten dimulai.

        Contoh implementasi :

        ```css
        div {
            margin: 20px;
            border: 2px solid black;
            padding: 10px;
            }
        ```

Pertanyaan 4 : Jelaskan konsep flex box dan grid layout beserta kegunaannya!

    Flexbox adalah sebuah layout model yang memungkinkan elemen-elemen dalam suatu container untuk disusun secara fleksibel. Flexbox berguna untuk membuat tata letak yang responsif dan dinamis, seperti mengatur elemen secara horizontal atau vertikal, dan mengatur lebar atau tinggi elemen secara otomatis berdasarkan ruang yang tersedia.

    Grid Layout, CSS Grid adalah layout system yang lebih kompleks dari Flexbox, memungkinkan kamu untuk membuat tata letak dua dimensi (baris dan kolom). Grid berguna untuk membuat tata letak yang lebih rumit, seperti galeri gambar atau dashboard, karena memberikan kontrol lebih baik terhadap elemen-elemen dalam container.

Pertanyaan 5 : Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

    1. Implementasikan fungsi untuk menghapus dan mengedit product.
        kita dapat menambahkan fuction edit_product dan delete_product pada views.py dan jangan lupa di root pada urls.py
    
    2. Kustomisasi halaman login, register, dan tambah product semenarik mungkin.
        Pada tahap ini saya menggunakan css framework yaitu tailwind untuk mendesain halaman login.html, register.html, create_product.html. Dan membuatnya desain sebaik mungkin seperti ukuran text, warna background, warna text, dan lain sebagainya.

    3.  Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menamp          gambar dan pesan bahwa belum ada product yang terdaftar.
        Pada tahap ini, kita dapat mengisikan logika sederhana pada main.html, yaitu {% if not product %} dimana jika tidak ada product maka program akan menampilkan sedih-banget.png yang sudah tersimpan

    4. Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).
        Pada tahap ini kita dapat membuat card_info.html dalam direktori main/templates. Lalu kita dapat mendesain card sesuai selera kita menggunakan framework.

    5. Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
        Pada tahap ini kita dapat membuat href link pada card_product dan menghubungkannya dengan fuction edit_product dan delete_product pada views.py dengan hyperlink : 
            <a href="{% url 'main:edit_product' produk.pk %}"
            <a href="{% url 'main:delete_product' produk.pk %}"

    6. Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop
        

TUGAS 6

Pertanyaan 1 : jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!

    1. Interaktivitas yang lebih baik, JavaScript memungkinkan pengembang untuk menciptakan antarmuka pengguna (UI) yang dinamis dan interaktif. Elemen-elemen halaman dapat diubah atau diperbarui tanpa harus me-reload seluruh halaman, sehingga membuat pengalaman pengguna lebih baik.
    
    2. Pengolahan Data secara Real-Time, dengan JavaScript, aplikasi dapat memproses data di sisi klien secara real-time, seperti validasi input form sebelum dikirim ke server.

    3. Cross-Platform, javaScript adalah bahasa lintas platform, sehingga dapat berjalan di hampir semua browser modern dan digunakan untuk berbagai jenis perangkat (desktop, mobile).

        
Pertanyaan 2 : Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?

    Fungsi await digunakan untuk menunggu penyelesaian dari sebuah Promise sebelum melanjutkan eksekusi kode berikutnya. Saat digunakan dengan fetch(), await akan membuat kode menunggu hingga permintaan fetch() selesai dan respons diterima, tanpa memblokir eksekusi thread utama. Ini membantu memastikan bahwa kode yang bergantung pada hasil fetch() tidak dieksekusi sebelum datanya tersedia. Jika kita tidak menggunakan await, fetch() akan mengembalikan sebuah Promise, dan kode berikutnya akan dieksekusi sebelum respons dari server diterima. Ini dapat menyebabkan bug karena data yang diharapkan mungkin belum siap saat digunakan. Sebagai contoh, jika kita mencoba memanipulasi data dari server tanpa menunggu Promise selesai, kita akan mengakses data yang belum tersedia.

Pertanyaan 3 : Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?

    Django secara default menggunakan mekanisme CSRF (Cross-Site Request Forgery) untuk melindungi aplikasi dari serangan CSRF. Namun, ketika kita mengirimkan permintaan AJAX, permintaan POST perlu menyertakan token CSRF untuk dapat diproses. 

Pertanyaan 4 : Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?

    Pembersihan data di backend penting untuk:
        1. Terkait keamanan, validasi di frontend bisa saja dilewati, sehingga backend memberikan perlindungan terakhir.
        2. Konsistensi, Backend memastikan data yang disimpan selalu valid dan sesuai format.
        3. Backend menerima data dari berbagai sumber, bukan hanya frontend, sehingga validasi diperlukan untuk menjaga integritas data.

Pertanyaan 5 : Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

    1. Mengubah cards agar mendukung AJAX GET

        Hapus bagian conditional if pada main.html dan tambahkan line berikut
        <div id="product_entry_cards"></div>

    2. Buat sebuah fungsi JavaScript

        async function refreshProduct() {
            document.getElementById("product_entry_cards").innerHTML = "";
            document.getElementById("product_entry_cards").className = "";
            const productEntries = await getProduct();
            let htmlString = "";
            let classNameString = "";

            if (productEntries.length === 0) {
                classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
                htmlString = `
                    <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                        <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
                        <p class="text-center text-gray-600 mt-4">Belum ada data product pada Ecommers sate.</p>
                    </div>
                `;
            }
            else {
                classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full"
                productEntries.forEach((item) => {
                const name = DOMPurify.sanitize(item.fields.name);
                const description = DOMPurify.sanitize(item.fields.description);

                    htmlString += `
                    <div class="relative bg-white shadow-lg rounded-lg overflow-hidden hover:shadow-2xl transition-all duration-500 ease-in-out transform hover:scale-105">
                    
                    <div class="bg-pink-500 p-6 text-white">
                        <h3 class="text-2xl font-bold">${ item.fields.name }</h3>
                    </div>
                
                    
                    <div class="p-6 space-y-4">
                        
                        <div class="flex justify-between items-center">
                            <div>
                                <p class="text-lg font-semibold text-gray-600">Harga</p>
                                <p class="text-2xl font-bold text-green-500">Rp ${ item.fields.price }</p>
                            </div>
                        </div>
                
                        
                        <div>
                            <p class="text-lg font-semibold text-gray-600">Deskripsi</p>
                            <p class="text-gray-700">${ item.fields.description }</p>
                        </div>
                
                        
                        <div class="flex justify-between items-center">
                        <div>
                            <p class="text-lg font-semibold text-gray-600">Stok</p>
                            <!-- Logika untuk menampilkan pesan jika stok habis atau stok tersedia -->
                            <p class="text-2xl font-bold">
                                ${item.fields.quantity > 0 
                                    ? `<span class="text-green-500">${item.fields.quantity}</span>`
                                    : `<span class="text-red-500">Stok Habis</span>`
                                }
                            </p>
                        </div>
                        </div>

                
                        
                        <div class="flex justify-end space-x-2">
                            <a href="/edit-product/${item.pk}" class="flex items-center justify-center bg-yellow-500 hover:bg-yellow-600 text-white font-semibold py-2 px-4 rounded transition-all duration-300 transform hover:scale-110">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" viewBox="0 0 20 20" fill="currentColor">
                                    <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                                </svg>
                                Edit
                            </a>
                            <a href="/delete/${item.pk}" class="flex items-center justify-center bg-red-500 hover:bg-red-600 text-white font-semibold py-2 px-4 rounded transition-all duration-300 transform hover:scale-110">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                                </svg>
                                Hapus
                            </a>
                        </div>
                    </div>
                </div>
                    `;
                });
            }
            document.getElementById("product_entry_cards").className = classNameString;
            document.getElementById("product_entry_cards").innerHTML = htmlString;
        }

    3. Mengambil data product pengguna yang login dengan AJAX GET

        1. modifikasi fungsi show_json agar mengambil data pemgguna login

            def show_json(request):
            
                data = Product.objects.filter(user=request.user)
                return HttpResponse(serializers.serialize('json', data), content_type='application/json')

        2. Buat fungsi JavaSript

            async function getproductEntries(){
                return fetch("{% url 'main:show_json' %}").then((res) => res.json())
            }

        3. Tombol untuk membuka modal dengan form untuk menambah produk

            buat sebuah fungsi yang akan menunjukkan modal
            function showModal() {
                const modal = document.getElementById('crudModal');
                const modalContent = document.getElementById('crudModalContent');

                modal.classList.remove('hidden'); 
                setTimeout(() => {
                    modalContent.classList.remove('opacity-0', 'scale-95');
                    modalContent.classList.add('opacity-100', 'scale-100');
                }, 50); 
            }

        4. Buat tommbol yang akan membuka modal pada halaman utama
        
            <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-lime-700 hover:bg-lime-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105" onclick="showModal();">
            Add New Product by AJAX
            </button>

        5. Buat fungsi view yang menambahkan product

            @csrf_exempt
            @require_POST
            def add_product_ajax(request):
                name = strip_tags(request.POST.get("name"))
                price = strip_tags(request.POST.get("price"))
                description = strip_tags(request.POST.get("description"))
                quantity = strip_tags(request.POST.get("quantity"))
                user = request.user

                new_product = Product(
                    name=name, description=description,
                    price=price,
                    user=user
                )
                new_product.save()

                return HttpResponse(b"CREATED", status=201)

        6. Buat path yang mengarah pada fungsi yang baru dibuat
            path('create-product-ajax/', add_product_ajax, name="add_product_ajax"),

        7.Menghubungkan form modal dengan path yang baru dibuat

            function addProduct() {
                fetch("{% url 'main:add_product_ajax' %}", {
                method: "POST",
                body: new FormData(document.querySelector('#ProductForm')),
                })
                .then(response => refreshProduct())

                document.getElementById("ProductForm").reset(); 
                document.querySelector("[data-modal-toggle='crudModal']").click();

                return false;
            }
            document.getElementById("ProductForm").addEventListener("submit", (e) => {
                e.preventDefault();
                addProduct();
            })

        8. Refresh halaman utama untuk melihat data baru
            panggil fungsi refresh yang telah dibuat
                refreshProduct();




 





