from flask import *
import sqlite3
import json
import os
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

db = sqlite3.connect("data/database.db", check_same_thread=False)
cursor = db.cursor()
#create database with id automate generate

command = """CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    username TEXT, 
    password TEXT, 
    status TEXT, 
    nama TEXT,
    registrasi TEXT, 
    wjik VARCHAR(255),
    tanggal_registrasi TEXT,
    tanggal_menikah TEXT,
    Alamat Text
    )"""
cursor.execute(command)
command = """CREATE TABLE IF NOT EXISTS baptis(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nama_lengkap TEXT,
    jenis_kelamin TEXT,
    wijk TEXT,
    tempat_lahir TEXT,
    tanggal_lahir TEXT,
    tanggal_baptis TEXT
    )"""
cursor.execute(command)
command = """CREATE TABLE IF NOT EXISTS sidi(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nama_lengkap TEXT,
    jenis_kelamin TEXT,
    wijk TEXT,
    tempat_lahir TEXT,
    tanggal_lahir TEXT,
    tanggal_baptis TEXT,
    tanggal_sidi TEXT
    )"""
cursor.execute(command)
command = """CREATE TABLE IF NOT EXISTS anak_lahir(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nama_lengkap TEXT,
    jenis_kelamin TEXT,
    wijk TEXT,
    tempat_lahir TEXT,
    tanggal_lahir TEXT
    )"""
cursor.execute(command)
command = """CREATE TABLE IF NOT EXISTS rpp(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nama_lengkap TEXT,
    jenis_kelamin TEXT,
    wijk TEXT,
    tanggal_rpp TEXT,
    alasan TEXT
    )"""
cursor.execute(command)
command = """CREATE TABLE IF NOT EXISTS martumpol(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nama_lengkap_laki TEXT,
    nama_ayah_laki TEXT,
    nama_ibu_laki TEXT,
    tempat_lahir_laki TEXT,
    wijk_laki TEXT,
    nama_lengkap_perempuan TEXT,
    nama_ayah_perempuan TEXT,
    nama_ibu_perempuan TEXT,
    tempat_lahir_perempuan TEXT,
    wijk_perempuan TEXT,
    tanggal_martumpol TEXT,
    pukul_martumpol TEXT
    )"""
cursor.execute(command)
command = """CREATE TABLE IF NOT EXISTS pernikahan(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nama_lengkap_laki TEXT,
    nama_ayah_laki TEXT,
    nama_ibu_laki TEXT,
    tempat_lahir_laki TEXT,
    wijk_laki TEXT,
    nama_lengkap_perempuan TEXT,
    nama_ayah_perempuan TEXT,
    nama_ibu_perempuan TEXT,
    tempat_lahir_perempuan TEXT,
    wijk_perempuan TEXT,
    tanggal_pernikahan TEXT,
    pukul_pernikahan TEXT
    )"""
cursor.execute(command)
command = """CREATE TABLE IF NOT EXISTS meninggal(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nama_lengkap TEXT,
    jenis_kelamin TEXT,
    wijk TEXT,
    monding TEXT
    )"""
cursor.execute(command)
command = """CREATE TABLE IF NOT EXISTS kebaktian(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nama_kebaktian TEXT,
    tanggal TEXT,
    pengkhotbah TEXT,
    liturgis TEXT,
    jumlah_perhalado INTEGER,
    keterangan TEXT,
    jenis_ibadah TEXT,
    jumlah_laki INTEGER,
    jumlah_perempuan INTEGER,
    total_jemaat INTEGER,
    bapak INTEGER,
    ibu INTEGER,
    naposo INTEGER,
    remaja INTEGER,
    sekolah_minggu INTEGER
    )"""
cursor.execute(command)
command = """CREATE TABLE IF NOT EXISTS pelayanan(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nama_lengkap TEXT,
    jenis_kelamin TEXT,
    status_pelayanan TEXT,
    jenis_pelayanan TEXT,
    tanggal_tahbisan TEXT
    )"""
cursor.execute(command)
command = """CREATE TABLE IF NOT EXISTS keluarga(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    myid INTEGER, 
    nama TEXT,
    status TEXT,
    jenis_kelamin TEXT,
    tempat_lahir TEXT,
    tanggal_lahir TEXT,
    tanggal_baptis TEXT,
    tanggal_sidi TEXT,
    pekerjaan TEXT,
    pendidikan TEXT,
    alamat TEXT,
    wijk TEXT,
    registrasi TEXT
    )"""
cursor.execute(command)
command = """CREATE TABLE IF NOT EXISTS bulanan(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    username TEXT,
    nama TEXT,
    nominal INTEGER,
    bulan TEXT,
    bukti TEXT,
    status TEXT
    )"""
cursor.execute(command)
command = """CREATE TABLE IF NOT EXISTS hamauliateon(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    username TEXT,
    nama TEXT,
    huria INTEGER,
    pembangunan INTEGER,
    diakonia INTEGER,
    pendeta INTEGER,
    sintua INTEGER,
    perhalado INTEGER,
    ama INTEGER,
    ina INTEGER,
    nhkbp INTEGER,
    remaja INTEGER,
    sekolah_minggu INTEGER,
    pemusik INTEGER,
    multimedia INTEGER,
    song_leader INTEGER,
    total INTEGER,
    bukti TEXT,
    status TEXT,
    nama_keluarga TEXT
    )"""
cursor.execute(command)
command = """ CREATE TABLE IF NOT EXISTS financial_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_minggu TEXT,
            tanggal TEXT,
            pemasukan_pagi INTEGER,
            pemasukan_sore INTEGER,
            pemasukan_sekolah INTEGER,
            pemasukan_kasual INTEGER,
            pemasukan_partangiangan INTEGER,
            pemasukan_kategori INTEGER,
            transitori INTEGER,
            pemasukan_lainnya INTEGER,
            konven_pendeta INTEGER,
            transport INTEGER,
            rumah_tangga INTEGER,
            diakonia INTEGER,
            koinonia INTEGER,
            marturia INTEGER,
            biaya_operasional INTEGER,
            pengeluaran_lainnya INTEGER,
            total_pemasukan INTEGER,
            total_pengeluaran INTEGER
        )"""
cursor.execute(command)

app = Flask(__name__, static_folder="Static", template_folder="Templates")
UPLOAD_FOLDER = 'static/pdf'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "y1A0A2m9U3A8n4b7b5I6b1t5y2l6d"

def index():
    with open("data/warta_jemaat.json", "r") as f:
        data = json.load(f)
    if len(data) > 3:
        #just take 3 latest data from data
        warta_jemaat = data[-3:]
    else:
        warta_jemaat = data
    command = "SELECT * FROM pelayanan"
    cursor.execute(command)
    myData = cursor.fetchall()
    if len(myData) > 3:
        #just take 3 latest data from data
        pelayanan = myData[-3:]
    else:
        pelayanan = myData
    with open("data/berita.json", "r") as fil:
        beritadata = json.load(fil)
    if len(beritadata) > 3:
        #just take 3 latest data from data
        berita = beritadata[-3:]
    else:
        berita = beritadata
    if "status" in session:
        if session["status"] == "Admin":
            return render_template("User/index.html", warta_jemaat=warta_jemaat, pelayanan=pelayanan, berita=berita, logged="Admin")
        elif session["status"] == "Peserta":
            return render_template("User/index.html", warta_jemaat=warta_jemaat, pelayanan=pelayanan, berita=berita, logged="Peserta")
    else:
        return render_template("User/index.html", warta_jemaat=warta_jemaat, pelayanan=pelayanan, berita=berita, logged="Not Login")

# def warta_user():
#     with open("data/warta_jemaat.json", "r") as f:
#         data = json.load(f)
#     return render_template("User/warta.html", data=data)

def warta_user():
    # Load JSON data
    with open("data/warta_jemaat.json", "r") as f:
        data = json.load(f)
    page = request.args.get('page', 1, type=int)  # Get the current page number from query params
    per_page = 5  # Number of items per page
    total_pages = (len(data) + per_page - 1) // per_page  # Calculate total number of pages
    start = (page - 1) * per_page
    end = start + per_page
    paginated_data = data[start:end]  # Get the data for the current page
    logged = ""
    if session:
        logged = session["status"]
    return render_template("User/warta.html", data=paginated_data, page=page, total_pages=total_pages, logged=logged)

def login():
    error = request.args.get("error") or ""
    return render_template("User/login.html", error=error)

def login_admin():
    error = request.args.get("error") or ""
    return render_template("Admin/login_admin.html", error=error)

def signin_admin():
    username = request.form.get("username")
    password = request.form.get("password")
    kode = request.form.get("kode")
    if username == "Admin" and password == "Admin" and kode == "182101":
        session["username"] = username
        session["password"] = password
        session["status"] = "Admin"
        return redirect(url_for("dashboard"))
    else:
        return redirect("/login/admin?error=Data%20tidak%20valid")

def signin():
        username = request.form.get("username")
        password = request.form.get("password")
        print(username)
        print(password)
    # if username == "Admin" and password == "Admin":
    #     session["username"] = username
    #     session["password"] = password
    #     session["status"] = "Admin"
    #     return redirect(url_for("dashboard"))
    # else:
        command = f"SELECT * FROM user WHERE username='{username}' AND password='{password}'"
        cursor.execute(command)
        myData = cursor.fetchone()
        #add all of data from user into session
        if myData:
            myid, username, password, status, nama, registrasi, wijk, tanggal_registrasi, tanggal_menikah, alamat = myData
            session["id"] = myid
            session["username"] = username
            session["password"] = password
            session["status"] = status
            session["nama"] = nama
            session["registrasi"] = registrasi
            session["wijk"] = wijk
            session["tanggal_registrasi"] = tanggal_registrasi
            session["tanggal_menikah"] = tanggal_menikah
            session["alamat"] = alamat
            return redirect(url_for("index"))
        else:
            return redirect("/login?error=Data%20tidak%20valid")

def dashboard():
    if "status" in session:
        if session["status"] == "Admin":
            command = "SELECT * FROM user"
            cursor.execute(command)
            users = cursor.fetchall()
            users = len(users)
            command = f"SELECT * FROM keluarga"
            cursor.execute(command)
            data_keluarga = cursor.fetchall()
            laki = 0
            perempuan = 0
            for data in data_keluarga:
                if data[4] == "Perempuan":
                    perempuan += 1
                else:
                    laki += 1
            keluarga = len(data_keluarga)
            with open("data/warta_jemaat.json", "r") as file:
                data = json.load(file)
            data = len(data)
            command = f"SELECT * FROM bulanan"
            cursor.execute(command)
            bulanan = cursor.fetchall()
            nominal = 0
            jan = 0
            feb = 0
            mar = 0
            apr = 0
            may = 0
            jun = 0
            jul = 0
            aug = 0
            sep = 0
            okt = 0
            nov = 0
            dec = 0
            for i in bulanan:
                if i[6] == "verified":
                    if i[4] == "Januari":
                        jan += int(i[3])
                    elif i[4] == "Februari":
                        feb += int(i[3])
                    elif i[4] == "Maret":
                        mar += int(i[3])
                    elif i[4] == "April":
                        apr += int(i[3])
                    elif i[4] == "Mei":
                        may += int(i[3])
                    elif i[4] == "Juni":
                        jun += int(i[3])
                    elif i[4] == "Juli":
                        jul += int(i[3])
                    elif i[4] == "Agustus":
                        aug += int(i[3])
                    elif i[4] == "September":
                        sep += int(i[3])
                    elif i[4] == "Oktober":
                        okt += int(i[3])
                    elif i[4] == "November":
                        nov += int(i[3])
                    elif i[4] == "Desember":
                        dec += int(i[3])
                    nominal += int(i[3])
            command = f"SELECT * FROM hamauliateon"
            cursor.execute(command)
            hamauliateon = cursor.fetchall()
            total = 0
            for i in hamauliateon:
                if i[19] == "verified":
                    total += int(i[17])
            str_total = locale.currency(total, grouping=True)[:-3]
            command = f"SELECT * FROM financial_data"
            cursor.execute(command)
            financial_data = cursor.fetchall()
            pemasukan = 0
            pengeluaran = 0
            for i in financial_data:
                pemasukan += int(i[19])
                pengeluaran += int(i[20])
            total_kas = pemasukan - pengeluaran
            str_nominal = locale.currency(nominal, grouping=True)[:-3]
            str_total_kas = locale.currency(total_kas, grouping=True)[:-3]
            #pengambilan data dari warta_keuangan dari sini
            monthly_pemasukan = {
                "Jan": 0, "Feb": 0, "Mar": 0, "Apr": 0, "May": 0, 
                "Jun": 0, "Jul": 0, "Aug": 0, "Sep": 0, "Oct": 0, 
                "Nov": 0, "Dec": 0
            }
            monthly_pengeluaran = {
                "Jan": 0, "Feb": 0, "Mar": 0, "Apr": 0, "May": 0, 
                "Jun": 0, "Jul": 0, "Aug": 0, "Sep": 0, "Oct": 0, 
                "Nov": 0, "Dec": 0
            }
            monthly_nominal = {
                "Jan": 0, "Feb": 0, "Mar": 0, "Apr": 0, "May": 0, 
                "Jun": 0, "Jul": 0, "Aug": 0, "Sep": 0, "Oct": 0, 
                "Nov": 0, "Dec": 0
            }
            cursor.execute("""
                SELECT tanggal, total_pemasukan, total_pengeluaran 
                FROM financial_data
            """)
            rows = cursor.fetchall()
            # Process each row to calculate monthly totals
            for row in rows:
                tanggal, total_pemasukan, total_pengeluaran = row
                
                # Convert the date to month (e.g., "Jan", "Feb", etc.)
                month_str = datetime.strptime(tanggal, "%Y-%m-%d").strftime("%b")
                
                # Sum up total pemasukan and pengeluaran for each month
                monthly_pemasukan[month_str] += total_pemasukan if total_pemasukan else 0
                monthly_pengeluaran[month_str] += total_pengeluaran if total_pengeluaran else 0

            # Calculate monthly nominal (difference between pemasukan and pengeluaran)
            for month in monthly_pemasukan:
                monthly_nominal[month] = monthly_pemasukan[month] - monthly_pengeluaran[month]
            return render_template("Admin/dashboard.html", 
                                   users=users, 
                                   keluarga=keluarga,
                                   data=data,
                                   total=str_nominal,
                                   hamauliateon=str_total,
                                   laki=laki,
                                   perempuan=perempuan,
                                   total_kas=str_total_kas,
                                   jan=jan,
                                   feb=feb,
                                   mar=mar,
                                   apr=apr,
                                   may=may,
                                   jun=jun,
                                   jul=jul,
                                   aug=aug,
                                   sep=sep,
                                   oct=okt,
                                   nov=nov,
                                   dec=dec,
                                   kas=monthly_nominal
                                   )
    else:
        return redirect(url_for("index"))

def management_user():
    if "status" in session:
        if session["status"] == "Admin":
            with open("data/nama_wjik.txt", "r") as f:
                wijk = f.read().split("\n")
            command = "SELECT * FROM user"
            query = request.args.get("query")
            if query:
                command += f" WHERE username LIKE '%{query}%'"
            cursor.execute(command)
            users = cursor.fetchall()
            return render_template("Admin/management_user.html", users=users, wijk=wijk)
    else:
        return redirect(url_for("index"))

def adduser():
    if "status" in session:
        if session["status"] == "Admin":
            username = request.form.get("username")
            password = request.form.get("password")
            registrasi = request.form.get("registrasi")
            tanggal_registrasi = request.form.get("tanggal_registrasi")
            tanggal_menikah = request.form.get("tanggal_menikah")
            nama = request.form.get("nama")
            Alamat = request.form.get("alamat")
            wijk = request.form.get("wijk")
            status = "Peserta"
            command = f"INSERT INTO user(username, password, status, registrasi, tanggal_registrasi, tanggal_menikah, nama, Alamat, wjik) VALUES('{username}', '{password}', '{status}', '{registrasi}', '{tanggal_registrasi}', '{tanggal_menikah}', '{nama}', '{Alamat}', '{wijk}')"
            # command = f"INSERT INTO user(username, password, status) VALUES('{username}', '{password}', '{status}')"
            cursor.execute(command)
            db.commit()
            new_json = []
            filename = f"data/{username}.json"
            #create a new json file
            with open(filename, "w") as f:
                json.dump(new_json, f)
            return redirect(url_for("management_user"))
    else:
        return redirect(url_for("index"))

def hapus():
    if "status" in session:
        if session["status"] == "Admin":
            id = request.args.get("id")
            command = f"DELETE FROM user WHERE id={id}"
            cursor.execute(command)
            db.commit()
            return redirect(url_for("management_user"))
    else:
        return redirect(url_for("index"))

def keluar():
    session.clear()
    return redirect(url_for("index"))

def ubah_data_jemaat():
    if "status" in session:
        if session["status"] == "Admin":
            with open("data/nama_wjik.txt", "r") as f:
                wjik = f.read().split("\n")
            print(wjik)
            command = "SELECT * FROM user"
            query = request.args.get("query")
            if query:
                command += f" WHERE username LIKE '%{query}%' OR nama LIKE '%{query}%' OR registrasi LIKE '%{query}%' OR wjik LIKE '%{query}%'"
            cursor.execute(command)
            users = cursor.fetchall()
            return render_template("Admin/ubah_data_jemaat.html", users=users, wjik=wjik)
    else:
        return redirect(url_for("index"))

def keluarga():
    if "status" in session:
        if session["status"] == "Admin":
            with open("data/nama_wjik.txt", "r") as f:
                wijk = f.read().split("\n")
            id = request.args.get("id")
            command = f"SELECT * FROM user WHERE id={id}"
            query = request.args.get("query")
            cursor.execute(command)
            user = cursor.fetchone()
            command = f"SELECT * FROM keluarga WHERE myid={id}"
            if query:
                command += f" AND nama LIKE '%{query}%'"
            cursor.execute(command)
            keluarga = cursor.fetchall()
            return render_template("Admin/data_keluarga.html", user=user, wijk=wijk, families=keluarga)
    else:
        return redirect(url_for("index"))

def edit_user():
    if "status" in session:
        if session["status"] == "Admin":
            id = request.args.get("id")
            registrasi = request.form.get("registrasi")
            tanggal_registrasi = request.form.get("tanggal_registrasi")
            tanggal_menikah = request.form.get("tanggal_menikah")
            nama = request.form.get("nama")
            Alamat = request.form.get("alamat")
            wijk = request.form.get("wijk")
            command = f"UPDATE user SET registrasi='{registrasi}', tanggal_registrasi='{tanggal_registrasi}', tanggal_menikah='{tanggal_menikah}', nama='{nama}', Alamat='{Alamat}', wjik='{wijk}' WHERE id={id}"
            cursor.execute(command)
            db.commit()
            return redirect(url_for("management_user"))

def baptis():
    if "status" in session:
        if session["status"] == "Admin":
            with open("data/nama_wjik.txt", "r") as f:
                wijk = f.read().split("\n")
            command = "SELECT * FROM baptis"
            query = request.args.get("query")
            if query:
                command += f" WHERE nama_lengkap LIKE '%{query}%'"
            cursor.execute(command)
            users = cursor.fetchall()
            return render_template("Admin/baptis.html", users=users, wijk=wijk)
    else:
        return redirect(url_for("index"))

def addbaptis():
    if "status" in session:
            nama_lengkap = request.form.get("nama_lengkap")
            jenis_kelamin = request.form.get("jenis_kelamin")
            tempat_lahir = request.form.get("tempat_lahir")
            tanggal_lahir = request.form.get("tanggal_lahir")
            wijk = request.form.get("wijk")
            tanggal_baptis = request.form.get("tanggal_baptis")
            command = f"INSERT INTO baptis(nama_lengkap, jenis_kelamin, tempat_lahir, tanggal_lahir, wijk, tanggal_baptis) VALUES('{nama_lengkap}', '{jenis_kelamin}', '{tempat_lahir}', '{tanggal_lahir}', '{wijk}', '{tanggal_baptis}')"
            cursor.execute(command)
            db.commit()
            if session["status"] == "Admin":
                return redirect(url_for("jemaat_baptis"))
            else:
                return redirect("/profile/jemaat_baptis")
    else:
        return redirect(url_for("index"))

def deletebaptis():
    if session["status"] == "Admin":
        id = request.args.get("id")
        command = f"DELETE FROM baptis WHERE id={id}"
        cursor.execute(command)
        db.commit()
        return redirect(url_for("jemaat_baptis"))
    else:
        return redirect(url_for("index"))

def sidi():
    if "status" in session:
        if session["status"] == "Admin":
            with open("data/nama_wjik.txt", "r") as f:
                wijk = f.read().split("\n")
            command = "SELECT * FROM sidi"
            query = request.args.get("query")
            if query:
                command += f" WHERE nama_lengkap LIKE '%{query}%'"
            cursor.execute(command)
            users = cursor.fetchall()
            return render_template("Admin/sidi.html", users=users, wijk=wijk)
    else:
        return redirect(url_for("index"))

def addsidi():
    print("debug 0")
    if "status" in session:
            nama_lengkap = request.form.get("nama_lengkap")
            jenis_kelamin = request.form.get("jenis_kelamin")
            tempat_lahir = request.form.get("tempat_lahir")
            tanggal_lahir = request.form.get("tanggal_lahir")
            tanggal_baptis = request.form.get("tanggal_baptis")
            tanggal_sidi = request.form.get("tanggal_sidi")
            wijk = request.form.get("wijk")
            command = f"INSERT INTO sidi(nama_lengkap, jenis_kelamin, tempat_lahir, tanggal_lahir, wijk, tanggal_baptis, tanggal_sidi) VALUES('{nama_lengkap}', '{jenis_kelamin}', '{tempat_lahir}', '{tanggal_lahir}', '{wijk}', '{tanggal_baptis}', '{tanggal_sidi}')"
            cursor.execute(command)
            db.commit()
            if session["status"] == "Admin":
                return redirect(url_for("jemaat_sidi"))
            else:
                print("debug 3")
                return redirect("/profile/jemaat_sidi")
    else:
        return redirect(url_for("index"))

def deletesidi():
    if session["status"] == "Admin":
        id = request.args.get("id")
        command = f"DELETE FROM sidi WHERE id={id}"
        cursor.execute(command)
        db.commit()
        return redirect(url_for("jemaat_sidi"))
    else:
        return redirect(url_for("index"))

def lahir():
    if "status" in session:
        if session["status"] == "Admin":
            with open("data/nama_wjik.txt", "r") as f:
                wijk = f.read().split("\n")
            query = request.args.get("query")
            command = "SELECT * FROM anak_lahir"
            if query:
                command += f" WHERE nama_lengkap LIKE '%{query}%' OR wijk LIKE '%{query}%'"
            cursor.execute(command)
            users = cursor.fetchall()
            return render_template("Admin/anak_lahir.html", users=users, wijk=wijk)
    else:
        return redirect(url_for("index"))

def addlahir():
    if "status" in session:
            nama_lengkap = request.form.get("nama_lengkap")
            jenis_kelamin = request.form.get("jenis_kelamin")
            tempat_lahir = request.form.get("tempat_lahir")
            tanggal_lahir = request.form.get("tanggal_lahir")
            wijk = request.form.get("wijk")
            command = f"INSERT INTO anak_lahir(nama_lengkap, jenis_kelamin, tempat_lahir, tanggal_lahir, wijk) VALUES('{nama_lengkap}', '{jenis_kelamin}', '{tempat_lahir}', '{tanggal_lahir}', '{wijk}')"
            cursor.execute(command)
            db.commit()
            if session["status"] == "Admin":
                return redirect(url_for("anak_lahir"))
            else:
                return redirect("/profile/anak_lahir")
    else:
        return redirect(url_for("index"))

def deletelahir():
    if session["status"] == "Admin":
        id = request.args.get("id")
        command = f"DELETE FROM anak_lahir WHERE id={id}"
        cursor.execute(command)
        db.commit()
        return redirect(url_for("anak_lahir"))
    else:
        return redirect(url_for("index"))

def rpp():
    if "status" in session:
        if session["status"] == "Admin":
            with open("data/nama_wjik.txt", "r") as f:
                wijk = f.read().split("\n")
            command = "SELECT * FROM rpp"
            query = request.args.get("query")
            if query:
                command += f" WHERE nama_lengkap LIKE '%{query}%' OR wijk LIKE '%{query}%'"
            cursor.execute(command)
            users = cursor.fetchall()
            return render_template("Admin/rpp.html", users=users, wijk=wijk)
    else:
        return redirect(url_for("index"))

def addrpp():
    if "status" in session:
        if session["status"] == "Admin":
            nama_lengkap = request.form.get("nama_lengkap")
            jenis_kelamin = request.form.get("jenis_kelamin")
            tanggal_rpp = request.form.get("tanggal_rpp")
            alasan = request.form.get("alasan")
            wijk = request.form.get("wijk")
            command = f"INSERT INTO rpp(nama_lengkap, jenis_kelamin, wijk, tanggal_rpp, alasan) VALUES('{nama_lengkap}', '{jenis_kelamin}', '{wijk}', '{tanggal_rpp}', '{alasan}')"
            cursor.execute(command)
            db.commit()
            return redirect(url_for("rpp"))
    else:
        return redirect(url_for("index"))

def deleterpp():
    if session["status"] == "Admin":
        id = request.args.get("id")
        command = f"DELETE FROM rpp WHERE id={id}"
        cursor.execute(command)
        db.commit()
        return redirect(url_for("rpp"))
    else:
        return redirect(url_for("index"))

def martumpol():
    if "status" in session:
        if session["status"] == "Admin":
            with open("data/nama_wjik.txt", "r") as f:
                wijk = f.read().split("\n")
            command = "SELECT * FROM martumpol"
            query = request.args.get("query")
            if query:
                command += f" WHERE nama_lengkap_laki LIKE '%{query}%' OR wijk_laki LIKE '%{query}%' OR nama_lengkap_perempuan LIKE '%{query}%' OR wijk_perempuan LIKE '%{query}%'"
            cursor.execute(command)
            users = cursor.fetchall()
            return render_template("Admin/martumpol.html", users=users, wijk=wijk)
    else:
        return redirect(url_for("index"))

def addmartumpol():
    if "status" in session:
            nama_lengkap_laki = request.form.get("nama_lengkap_laki")
            nama_ayah_laki = request.form.get("nama_ayah_laki")
            nama_ibu_laki = request.form.get("nama_ibu_laki")
            tempat_lahir_laki = request.form.get("tempat_lahir_laki")
            wijk_laki = request.form.get("wijk_laki")
            nama_lengkap_perempuan = request.form.get("nama_lengkap_perempuan")
            nama_ayah_perempuan = request.form.get("nama_ayah_perempuan")
            nama_ibu_perempuan = request.form.get("nama_ibu_perempuan")
            tempat_lahir_perempuan = request.form.get("tempat_lahir_perempuan")
            wijk_perempuan = request.form.get("wijk_perempuan")
            tanggal_martumpol = request.form.get("tanggal_martumpol")
            pukul_martumpol = request.form.get("pukul_martumpol")
            command = f"INSERT INTO martumpol(nama_lengkap_laki, nama_ayah_laki, nama_ibu_laki, tempat_lahir_laki, wijk_laki, nama_lengkap_perempuan, nama_ayah_perempuan, nama_ibu_perempuan, tempat_lahir_perempuan, wijk_perempuan, tanggal_martumpol, pukul_martumpol) VALUES ('{nama_lengkap_laki}', '{nama_ayah_laki}', '{nama_ibu_laki}', '{tempat_lahir_laki}', '{wijk_laki}', '{nama_lengkap_perempuan}', '{nama_ayah_perempuan}', '{nama_ibu_perempuan}', '{tempat_lahir_perempuan}', '{wijk_perempuan}', '{tanggal_martumpol}', '{pukul_martumpol}')"
            cursor.execute(command)
            db.commit()
            if session["status"] == "Admin":
                return redirect(url_for("martumpol"))
            else:
                return redirect("/profile/martumpal")
    else:
        return redirect(url_for("index"))

def deletemartumpol():
    if session["status"] == "Admin":
        id = request.args.get("id")
        command = f"DELETE FROM martumpol WHERE id={id}"
        cursor.execute(command)
        db.commit()
        return redirect(url_for("martumpol"))
    else:
        return redirect(url_for("index"))

def pernikahan():
    if "status" in session:
        if session["status"] == "Admin":
            with open("data/nama_wjik.txt", "r") as f:
                wijk = f.read().split("\n")
            command = "SELECT * FROM pernikahan"
            query = request.args.get("query")
            if query:
                command += f" WHERE nama_lengkap_laki LIKE '%{query}%' OR wijk_laki LIKE '%{query}%' OR nama_lengkap_perempuan LIKE '%{query}%' OR wijk_perempuan LIKE '%{query}%'"
            cursor.execute(command)
            users = cursor.fetchall()
            return render_template("Admin/pernikahan.html", users=users, wijk=wijk)
    else:
        return redirect(url_for("index"))

def addpernikahan():
    if "status" in session:
            nama_lengkap_laki = request.form.get("nama_lengkap_laki")
            nama_ayah_laki = request.form.get("nama_ayah_laki")
            nama_ibu_laki = request.form.get("nama_ibu_laki")
            tempat_lahir_laki = request.form.get("tempat_lahir_laki")
            wijk_laki = request.form.get("wijk_laki")
            nama_lengkap_perempuan = request.form.get("nama_lengkap_perempuan")
            nama_ayah_perempuan = request.form.get("nama_ayah_perempuan")
            nama_ibu_perempuan = request.form.get("nama_ibu_perempuan")
            tempat_lahir_perempuan = request.form.get("tempat_lahir_perempuan")
            wijk_perempuan = request.form.get("wijk_perempuan")
            tanggal_pernikahan = request.form.get("tanggal_pernikahan")
            pukul_pernikahan = request.form.get("pukul_pernikahan")
            command = f"INSERT INTO pernikahan(nama_lengkap_laki, nama_ayah_laki, nama_ibu_laki, tempat_lahir_laki, wijk_laki, nama_lengkap_perempuan, nama_ayah_perempuan, nama_ibu_perempuan, tempat_lahir_perempuan, wijk_perempuan, tanggal_pernikahan, pukul_pernikahan) VALUES ('{nama_lengkap_laki}', '{nama_ayah_laki}', '{nama_ibu_laki}', '{tempat_lahir_laki}', '{wijk_laki}', '{nama_lengkap_perempuan}', '{nama_ayah_perempuan}', '{nama_ibu_perempuan}', '{tempat_lahir_perempuan}', '{wijk_perempuan}', '{tanggal_pernikahan}', '{pukul_pernikahan}')"
            cursor.execute(command)
            db.commit()
            if session["status"] == "Admin":
                return redirect(url_for("pernikahan"))
            else:
                return redirect("/profile/pernikahan")
    else:
        return redirect(url_for("index"))

def deletepernikahan():
    if session["status"] == "Admin":
        id = request.args.get("id")
        command = f"DELETE FROM pernikahan WHERE id={id}"
        cursor.execute(command)
        db.commit()
        return redirect(url_for("pernikahan"))
    else:
        return redirect(url_for("index"))

def meninggal_dunia():
    if "status" in  session:
        if session["status"] == "Admin":
            with open("data/nama_wjik.txt", "r") as f:
                wijk = f.read().split("\n")
            command = "SELECT * FROM meninggal"
            query = request.args.get("query")
            if query:
                command += f" WHERE nama_lengkap LIKE '%{query}%' OR wijk LIKE '%{query}%' "
            cursor.execute(command)
            users = cursor.fetchall()
            return render_template("Admin/meninggal_dunia.html", users=users, wijk=wijk)
    else:
        return redirect(url_for("index"))

def addmeninggal():
    if "status" in session:
        if session["status"] == "Admin":
            nama_lengkap = request.form.get("nama_lengkap")
            jenis_kelamin = request.form.get("jenis_kelamin")
            monding = request.form.get("monding")
            wijk = request.form.get("wijk")
            command = f"INSERT INTO meninggal(nama_lengkap, jenis_kelamin, monding, wijk) VALUES('{nama_lengkap}', '{jenis_kelamin}', '{monding}', '{wijk}')"
            cursor.execute(command)
            db.commit()
            return redirect(url_for("meninggal_dunia"))
    else:
        return redirect(url_for("login"))

def deletemeninggal():
    if session["status"] == "Admin":
        id = request.args.get("id")
        command = f"DELETE FROM meninggal WHERE id={id}"
        cursor.execute(command)
        db.commit()
        return redirect(url_for("meninggal_dunia"))
    else:
        return redirect(url_for("index"))

def kegiatan_kebaktian():
    if "status" in session:
        if session["status"] == "Admin":
            command = "SELECT * FROM kebaktian"
            query = request.args.get("query")
            if query:
                command += f" WHERE nama_kebaktian LIKE '%{query}%' OR pengkhotbah LIKE '%{query}%' "
            cursor.execute(command)
            users = cursor.fetchall()
            return render_template("Admin/kegiatan_kebaktian.html", users=users)
    else:
        return redirect(url_for("index"))

def addkebaktian():
    if "status" in session:
            nama_kebaktian = request.form.get("nama_kebaktian")
            tanggal = request.form.get("tanggal")
            pengkhotbah = request.form.get("pengkhotbah")
            liturgis = request.form.get("liturgis")
            jumlah_perhalado= request.form.get("jumlah_perhalado")
            keterangan = request.form.get("keterangan")
            jenis_ibadah = request.form.get("jenis_ibadah")
            jumlah_laki = request.form.get("jumlah_laki")
            jumlah_perempuan= request.form.get("jumlah_perempuan")
            total_jemaat = request.form.get("total_jemaat")
            bapak = request.form.get("bapak")
            ibu = request.form.get("ibu")
            naposo = request.form.get("naposo")
            remaja = request.form.get("remaja")
            sekolah_minggu = request.form.get("sekolah_minggu")
            command = f"INSERT INTO kebaktian(nama_kebaktian, tanggal, pengkhotbah, liturgis, jumlah_perhalado, keterangan, jenis_ibadah, jumlah_laki, jumlah_perempuan, total_jemaat, bapak, ibu, naposo, remaja, sekolah_minggu) VALUES('{nama_kebaktian}', '{tanggal}', '{pengkhotbah}', '{liturgis}', '{jumlah_perhalado}', '{keterangan}', '{jenis_ibadah}', '{jumlah_laki}', '{jumlah_perempuan}', '{total_jemaat}', '{bapak}', '{ibu}', '{naposo}', '{remaja}', '{sekolah_minggu}')"
            cursor.execute(command)
            db.commit()
            return redirect(url_for("kegiatan_kebaktian"))

def deletekebaktian():
    if session["status"] == "Admin":
        id = request.args.get("id")
        command = f"DELETE FROM kebaktian WHERE id={id}"
        cursor.execute(command)
        db.commit()
        return redirect(url_for("kegiatan_kebaktian"))
    else:
        return redirect(url_for("index"))
    
def data_pelayanan():
    if "status" in session:
        if session["status"] == "Admin":
            with open("data/nama_wjik.txt", "r") as f:
                wijk = f.read().split("\n")
            command = "SELECT * FROM pelayanan"
            query = request.args.get("query")
            if query:
                command += f" WHERE nama_lengkap LIKE '%{query}%' OR jenis_kelamin LIKE '%{query}%' OR status_pelayanan LIKE '%{query}%' OR jenis_pelayanan LIKE '%{query}%' "
            cursor.execute(command)
            users = cursor.fetchall()
            return render_template("Admin/pelayanan.html", users=users, wijk=wijk)
    else:
        return redirect(url_for("index"))

def addpelayanan():
    if "status" in session:
            nama_lengkap = request.form.get("nama_lengkap")
            jenis_kelamin = request.form.get("jenis_kelamin")
            status_pelayanan = request.form.get("status_pelayanan")
            jenis_pelayanan = request.form.get("jenis_pelayanan")
            tanggal_tahbisan = request.form.get("tanggal_tahbisan")
            #masukkan data diatas ke database pelayanan
            command = f"INSERT INTO pelayanan(nama_lengkap, jenis_kelamin, status_pelayanan, jenis_pelayanan, tanggal_tahbisan) VALUES('{nama_lengkap}', '{jenis_kelamin}', '{status_pelayanan}', '{jenis_pelayanan}', '{tanggal_tahbisan}')"
            cursor.execute(command)
            db.commit()
            return redirect(url_for("data_pelayanan"))
    else:
        return redirect(url_for("login"))

def deletepelayanan():
    if session["status"] == "Admin":
        id = request.args.get("id")
        command = f"DELETE FROM pelayanan WHERE id={id}"
        cursor.execute(command)
        db.commit()
        return redirect(url_for("data_pelayanan"))
    else:
        return redirect(url_for("index"))

def warta():
    if "status" in session:
        if session["status"] == "Admin":
            with open("data/warta_jemaat.json", "r") as file:
                data = json.load(file)
            print(data)
            return render_template("Admin/warta.html", data=data)
    else:
        return redirect(url_for("login"))
    
def addwarta():
    file = request.files.get("warta_file")
    if file.filename == '':
        return "No file selected"
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
    with open("data/warta_jemaat.json", "r") as fil:
        data = json.load(fil)
    new_data = {
        "judul": request.form.get("namaWarta"),
        "tanggal": request.form.get("tanggal"),
        "deskripsi": request.form.get("deskripsi"),
        "file": str(filepath)
    }
    data.append(new_data)
    with open("data/warta_jemaat.json", "w") as fil:
        json.dump(data, fil)
    return redirect(url_for("warta"))

def deletewarta():
    if session["status"] == "Admin":
        myid = request.args.get("id")
        myid = int(myid) - 1
        with open("data/warta_jemaat.json", "r") as fil:
            data = json.load(fil)
        data_remove = data[myid]
        data.remove(data_remove)
        with open("data/warta_jemaat.json", "w") as fil:
            json.dump(data, fil)
        return redirect(url_for("warta"))
    else:
        return redirect(url_for("index"))

def berita():
    if "status" in session:
        if session["status"] == "Admin":
            with open("data/berita.json", "r") as file:
                data = json.load(file)
            return render_template("Admin/berita.html", data=data)
    else:
        return redirect(url_for("login"))
    
def add_berita_page():
    if "status" in session:
        if session["status"] == "Admin":
            return render_template("Admin/add_berita.html")
    else:
        return redirect(url_for("login"))

def addberita():
    if "status" in session:
        judul = request.form.get("judulberita")
        isi = request.form.get("isiberita")
        if len(isi) > 50:
            deskripsi = isi[:50] + "..."
        else:
            deskripsi = isi
        with open("data/berita.json", "r") as file:
            data = json.load(file)
        #ambil tanggal dengan format hh//mm/yyyy
        tanggal = datetime.now().strftime("%d//%m//%Y")
        new_data = {
            "judul": judul,
            "isi": isi,
            "tanggal": tanggal,
            "deskripsi": deskripsi
        }
        data.append(new_data)
        with open("data/berita.json", "w") as file:
            json.dump(data, file)
        return redirect(url_for("berita"))
    else:
        return redirect(url_for("login"))

def deleteberita():
    if session["status"] == "Admin":
        myid = request.args.get("id")
        myid = int(myid) - 1
        with open("data/berita.json", "r") as fil:
            data = json.load(fil)
        data_remove = data[myid]
        data.remove(data_remove)
        with open("data/berita.json", "w") as fil:
            json.dump(data, fil)
        return redirect(url_for("warta"))
    else:
        return redirect(url_for("index"))

def pembayaran():
    if "status" in session:
        if session["status"] == "Admin":
            command = f"SELECT * FROM bulanan"
            cursor.execute(command)
            query = request.args.get("query")
            if query:
                command += f" WHERE username LIKE '%{query}%' OR nama LIKE '%{query}%' OR bulan LIKE '%{query}%'"
            cursor.execute(command)
            users = cursor.fetchall()
            return render_template("Admin/bulanan.html", users=users)
    else:
        return redirect(url_for("index"))
    
def verify_pembayaran():
    if session["status"] == "Admin":
        id = request.args.get("id")
        command = f"UPDATE bulanan SET status='verified' WHERE id={id}"
        cursor.execute(command)
        db.commit()
        command = f"SELECT * FROM bulanan WHERE id={id}"
        cursor.execute(command)
        user = cursor.fetchone()
        nama = "Bulanan"
        tanggal = datetime.now().strftime("%Y-%m-%d")
        total_pemasukan = user[3]
        data = (nama, tanggal, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0, total_pemasukan, 0)
        command = """
                INSERT INTO financial_data (
                nama_minggu, tanggal, pemasukan_pagi, pemasukan_sore,
                pemasukan_sekolah, pemasukan_kasual, pemasukan_partangiangan,
                pemasukan_kategori, transitori, pemasukan_lainnya,
                konven_pendeta, transport, rumah_tangga, diakonia, koinonia,
                marturia, biaya_operasional, pengeluaran_lainnya, total_pemasukan, total_pengeluaran
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
        cursor.execute(command, data)
        db.commit()
        return redirect(url_for("pembayaran"))
    else:
        return redirect(url_for("index"))

def more_info():
    if session["status"] == "Admin":
        id = request.args.get("id")
        page = request.args.get("page")
        command = f"SELECT * FROM {page} WHERE id={id}"
        cursor.execute(command)
        user = cursor.fetchone()
        print(user)
        return render_template("more_info.html", user=user, page=page)
    else:
        return redirect(url_for("index"))

def show_bukti(filename):
        image_path = os.path.join(app.static_folder, 'pdf', filename)
        if not os.path.isfile(image_path):
            abort(404)
        print(f"pdf/{filename}")
        if filename.endswith('.pdf'):
            return render_template("Admin/bukti.html", filename=f"pdf/{filename}", pdf=True)
        else:
            if session and session["status"] == "Admin":
                return render_template("Admin/bukti.html", filename=f"pdf/{filename}", pdf=False)
            else:
                return redirect(url_for("index"))

def deletebulanan():
    if session["status"] == "Admin":
        id = request.args.get("id")
        command = f"DELETE FROM bulanan WHERE id={id}"
        cursor.execute(command)
        db.commit()
        return redirect(url_for("pembayaran"))
    else:
        return redirect(url_for("index"))

def addbulanan_admin():
    if "status" in session:
        username = "None"
        nama_keluarga = request.form.get('nama')
        nominal_persembahan = request.form.get('nominal')
        persembahan_bulan = request.form.get('bulan')
        status = request.form.get("status")
        bukti_persembahan = request.files.get('bukti')
        file_path = None
        print(bukti_persembahan)
        if bukti_persembahan:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], bukti_persembahan.filename)
            bukti_persembahan.save(file_path)
        
        command = f"INSERT INTO bulanan (username, nama, nominal, bulan, bukti, status) VALUES ('{username}', '{nama_keluarga}', {nominal_persembahan}, '{persembahan_bulan}', '{file_path}', '{status}') "
        cursor.execute(command)
        db.commit()
        if status == "verified":
            nama = "Bulanan bulan " + persembahan_bulan
            tanggal = datetime.now().strftime("%Y-%m-%d")
            total_pemasukan = nominal_persembahan
            data = (nama, tanggal, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0, total_pemasukan, 0)
            command = """
                    INSERT INTO financial_data (
                    nama_minggu, tanggal, pemasukan_pagi, pemasukan_sore,
                    pemasukan_sekolah, pemasukan_kasual, pemasukan_partangiangan,
                    pemasukan_kategori, transitori, pemasukan_lainnya,
                    konven_pendeta, transport, rumah_tangga, diakonia, koinonia,
                    marturia, biaya_operasional, pengeluaran_lainnya, total_pemasukan, total_pengeluaran
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """
            cursor.execute(command, data)
            db.commit()
        return redirect(url_for("pembayaran"))
    else:
        return redirect(url_for("index"))

def verify_hamauliateon():
    if session["status"] == "Admin":
        id = request.args.get("id")
        #create sql command set status into verified where id is from variable call id
        command = f"UPDATE hamauliateon SET status='verified' WHERE id={id}"
        cursor.execute(command)
        db.commit()
        command = f"SELECT * FROM hamauliateon WHERE id={id}"
        cursor.execute(command)
        user = cursor.fetchone()
        nama = "Hamauliateon"
        tanggal = datetime.now().strftime("%Y-%m-%d")
        total_pemasukan = user[17]
        data = (nama, tanggal, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0, total_pemasukan, 0)
        command = """
                INSERT INTO financial_data (
                nama_minggu, tanggal, pemasukan_pagi, pemasukan_sore,
                pemasukan_sekolah, pemasukan_kasual, pemasukan_partangiangan,
                pemasukan_kategori, transitori, pemasukan_lainnya,
                konven_pendeta, transport, rumah_tangga, diakonia, koinonia,
                marturia, biaya_operasional, pengeluaran_lainnya, total_pemasukan, total_pengeluaran
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
        cursor.execute(command, data)
        db.commit()
        return redirect(url_for("hamauliateon_admin"))
    else:
        return redirect(url_for("index"))

def deletehamauliateon():
    if session["status"] == "Admin":
        id = request.args.get("id")
        command = f"DELETE FROM hamauliateon WHERE id={id}"
        cursor.execute(command)
        db.commit()
        return redirect(url_for("hamauliateon_admin"))
    else:
        return redirect(url_for("index"))

def hamauliateon_admin():
    if "status" in session:
        if session["status"] == "Admin":
            command = f"SELECT * FROM hamauliateon"
            query = request.args.get("query")
            if query:
                command += f" WHERE username LIKE '%{query}%' OR nama LIKE '%{query}%'"
            cursor.execute(command)
            users = cursor.fetchall()
            return render_template("Admin/hamauliateon.html", users=users)
    else:
        return redirect(url_for("index"))

def finansial_data():
    if "status" in session:
        if session["status"] == "Admin":
            return render_template("Admin/warta_keuangan.html")
    else:
        return redirect(url_for("index"))
    
def finansial_page():
    if session and session["status"] == "Admin":
        command = f"SELECT * FROM financial_data"
        cursor.execute(command)
        users = cursor.fetchall()
        pemasukan = 0
        pengeluaran = 0
        for i in users:
            pemasukan += int(i[19])
            pengeluaran += int(i[20])
        total = pemasukan - pengeluaran
        str_pemasukan = locale.currency(pemasukan, grouping=True)[:-3]
        str_pengeluaran = locale.currency(pengeluaran, grouping=True)[:-3]
        str_total = locale.currency(total, grouping=True)[:-3]
        query = request.args.get("query")
        if query:
            command += f" WHERE nama_minggu LIKE '%{query}%'"
        cursor.execute(command)
        users = cursor.fetchall()
        return render_template("Admin/warta_keuangan_page.html", users=users, pemasukan=str_pemasukan, pengeluaran=str_pengeluaran, total=str_total)
    else:
        return redirect(url_for("index"))

def finansial_edit():
    if session and session["status"] == "Admin":
        req = request.args.get("id")
        command = f"SELECT * FROM financial_data WHERE id={req}"
        cursor.execute(command)
        user = cursor.fetchone()
        return render_template("Admin/warta_keuangan_edit.html", user=user)
    else:
        return redirect(url_for("index"))

def submit_financial_data():
    if "status" in session:
        if session["status"] == "Admin":
            nama = request.form['namaMinggu']
            tanggal = request.form['tanggal']
            aa = request.form.get('pemasukanPagi', 0)
            ab = request.form.get('pemasukanSore', 0)
            ac = request.form.get('pemasukanSekolah', 0)
            ad = request.form.get('pemasukanKasual', 0)
            ae = request.form.get('pemasukanPartangiangan', 0)
            af = request.form.get('pemasukanKategori', 0)
            ag = request.form.get('transitori', 0)
            ai = request.form.get('pemasukanLainnya', 0)
            ba = request.form.get('konvenPendeta', 0)
            bb = request.form.get('transport', 0)
            bc = request.form.get('rumahTangga', 0)
            bd = request.form.get('diakonia', 0)
            be = request.form.get('koinonia', 0)
            bf = request.form.get('marturia', 0)
            bg = request.form.get('biayaOperasional', 0)
            bh = request.form.get('pengeluaranLainnya', 0)
            total_pemasukan = int(aa) + int(ab) + int(ac) + int(ad) + int(ae) + int(af) + int(ag) + int(ai)
            total_pengeluaran = int(ba) + int(bb) + int(bc) + int(bd) + int(be) + int(bf) + int(bg) + int(bh)
            data = (nama, tanggal, aa, ab, ac, ad,ae,af,ag,ai,ba,bb,bc,bd,be,bf,bg,bh, total_pemasukan, total_pengeluaran)
            command = """
                INSERT INTO financial_data (
                nama_minggu, tanggal, pemasukan_pagi, pemasukan_sore,
                pemasukan_sekolah, pemasukan_kasual, pemasukan_partangiangan,
                pemasukan_kategori, transitori, pemasukan_lainnya,
                konven_pendeta, transport, rumah_tangga, diakonia, koinonia,
                marturia, biaya_operasional, pengeluaran_lainnya, total_pemasukan, total_pengeluaran
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(command, data)
            db.commit()
            return(redirect(url_for("warta_keuangan")))
    else:
        return redirect(url_for("index"))

def edit_financial_data():
    if "status" in session:
        if session["status"] == "Admin":
            id = request.form['id']
            nama = request.form['namaMinggu']
            tanggal = request.form['tanggal']
            aa = request.form.get('pemasukanPagi', 0)
            ab = request.form.get('pemasukanSore', 0)
            ac = request.form.get('pemasukanSekolah', 0)
            ad = request.form.get('pemasukanKasual', 0)
            ae = request.form.get('pemasukanPartangiangan', 0)
            af = request.form.get('pemasukanKategori', 0)
            ag = request.form.get('transitori', 0)
            ai = request.form.get('pemasukanLainnya', 0)
            ba = request.form.get('konvenPendeta', 0)
            bb = request.form.get('transport', 0)
            bc = request.form.get('rumahTangga', 0)
            bd = request.form.get('diakonia', 0)
            be = request.form.get('koinonia', 0)
            bf = request.form.get('marturia', 0)
            bg = request.form.get('biayaOperasional', 0)
            bh = request.form.get('pengeluaranLainnya', 0)
            total_pemasukan = int(aa) + int(ab) + int(ac) + int(ad) + int(ae) + int(af) + int(ag) + int(ai)
            total_pengeluaran = int(ba) + int(bb) + int(bc) + int(bd) + int(be) + int(bf) + int(bg) + int(bh)
            data = (nama, tanggal, aa, ab, ac, ad,ae,af,ag,ai,ba,bb,bc,bd,be,bf,bg,bh, total_pemasukan, total_pengeluaran, id)
            #make command UPDATE data finansial_data where id is id
            command = f"""
                        UPDATE financial_data
                        SET nama_minggu = ?,
                            tanggal = ?,
                            pemasukan_pagi = ?,
                            pemasukan_sore = ?,
                            pemasukan_sekolah = ?,
                            pemasukan_kasual = ?,
                            pemasukan_partangiangan = ?,
                            pemasukan_kategori = ?,
                            transitori = ?,
                            pemasukan_lainnya = ?,
                            konven_pendeta = ?,
                            transport = ?,
                            rumah_tangga = ?,
                            diakonia = ?,
                            koinonia = ?,
                            marturia = ?,
                            biaya_operasional = ?,
                            pengeluaran_lainnya = ?,
                            total_pemasukan = ?,
                            total_pengeluaran = ?
                            WHERE id = ?
                            """
            cursor.execute(command, data)
            db.commit()
            return(redirect(url_for("warta_keuangan")))
    else:
        return redirect(url_for("index"))

def editlahir():
    if "status" in session:
        if session["status"] == "Admin":
            id = request.form['modal_id']
            nama_lengkap = request.form['modal_nama_lengkap']
            jenis_kelamin = request.form['modal_jenis_kelamin']
            wijk = request.form['modal_wijk']
            tempat_lahir = request.form['modal_tempat_lahir']
            tanggal_lahir = request.form['modal_tanggal_lahir']
            command = f"""
                        UPDATE anak_lahir
                        SET nama_lengkap = '{nama_lengkap}',
                            jenis_kelamin = '{jenis_kelamin}',
                            wijk = '{wijk}',
                            tempat_lahir = '{tempat_lahir}',
                            tanggal_lahir = '{tanggal_lahir}'
                        WHERE id = {id}
                        """
            cursor.execute(command)
            db.commit()
            return(redirect(url_for("anak_lahir")))
    else:
        return redirect(url_for("index"))

def editbaptis():
    if "status" in session:
        if session["status"] == "Admin":
            id = request.form['modal_id']
            nama_lengkap = request.form['modal_nama_lengkap']
            jenis_kelamin = request.form['modal_jenis_kelamin']
            wijk = request.form['modal_wijk']
            tempat_lahir = request.form['modal_tempat_lahir']
            tanggal_lahir = request.form['modal_tanggal_lahir']
            tanggal_baptis = request.form['modal_tanggal_baptis']
            command = f"""
                UPDATE baptis
                SET nama_lengkap = '{nama_lengkap}',
                    jenis_kelamin = '{jenis_kelamin}',
                    wijk = '{wijk}',
                    tempat_lahir = '{tempat_lahir}',
                    tanggal_lahir = '{tanggal_lahir}',
                    tanggal_baptis = '{tanggal_baptis}'
                WHERE id = {id}
                """
            cursor.execute(command)
            db.commit()
            return(redirect(url_for("jemaat_baptis")))
    else:
        return redirect(url_for("index"))

def editmartumpol():
    if "status" in session:
        if session["status"] == "Admin":
            id = request.form['modal_id']
            nama_lengkap_laki = request.form['modal_nama_lengkap_laki']
            nama_ayah_laki = request.form['modal_nama_ayah_laki']
            nama_ibu_laki = request.form['modal_nama_ibu_laki']
            tempat_lahir_laki = request.form['modal_tempat_lahir_laki']
            wijk_laki = request.form['modal_wijk_laki']
            
            nama_lengkap_perempuan = request.form['modal_nama_lengkap_perempuan']
            nama_ayah_perempuan = request.form['modal_nama_ayah_perempuan']
            nama_ibu_perempuan = request.form['modal_nama_ibu_perempuan']
            tempat_lahir_perempuan = request.form['modal_tempat_lahir_perempuan']
            wijk_perempuan = request.form['modal_wijk_perempuan']
            
            tanggal_martumpol = request.form['modal_tanggal_martumpol']
            pukul_martumpol = request.form['modal_pukul_martumpol']
            cursor.execute("""
                UPDATE martumpol
                SET nama_lengkap_laki = ?,
                    nama_ayah_laki = ?,
                    nama_ibu_laki = ?,
                    tempat_lahir_laki = ?,
                    wijk_laki = ?,
                    nama_lengkap_perempuan = ?,
                    nama_ayah_perempuan = ?,
                    nama_ibu_perempuan = ?,
                    tempat_lahir_perempuan = ?,
                    wijk_perempuan = ?,
                    tanggal_martumpol = ?,
                    pukul_martumpol = ?
                WHERE id = ?
            """, (
                nama_lengkap_laki,
                nama_ayah_laki,
                nama_ibu_laki,
                tempat_lahir_laki,
                wijk_laki,
                nama_lengkap_perempuan,
                nama_ayah_perempuan,
                nama_ibu_perempuan,
                tempat_lahir_perempuan,
                wijk_perempuan,
                tanggal_martumpol,
                pukul_martumpol,
                id
            ))
            db.commit()
            return(redirect(url_for("martumpol")))
    else:
        return redirect(url_for("index"))

def editpernikahan():
    if "status" in session:
        if session["status"] == "Admin":
            id = request.form['modal_id']
            nama_lengkap_laki = request.form['modal_nama_lengkap_laki']
            nama_ayah_laki = request.form['modal_nama_ayah_laki']
            nama_ibu_laki = request.form['modal_nama_ibu_laki']
            tempat_lahir_laki = request.form['modal_tempat_lahir_laki']
            wijk_laki = request.form['modal_wijk_laki']
            
            nama_lengkap_perempuan = request.form['modal_nama_lengkap_perempuan']
            nama_ayah_perempuan = request.form['modal_nama_ayah_perempuan']
            nama_ibu_perempuan = request.form['modal_nama_ibu_perempuan']
            tempat_lahir_perempuan = request.form['modal_tempat_lahir_perempuan']
            wijk_perempuan = request.form['modal_wijk_perempuan']
            
            tanggal_pernikahan = request.form['modal_tanggal_pernikahan']
            pukul_pernikahan = request.form['modal_pukul_pernikahan']
            cursor.execute("""
                UPDATE pernikahan
                SET nama_lengkap_laki = ?,
                    nama_ayah_laki = ?,
                    nama_ibu_laki = ?,
                    tempat_lahir_laki = ?,
                    wijk_laki = ?,
                    nama_lengkap_perempuan = ?,
                    nama_ayah_perempuan = ?,
                    nama_ibu_perempuan = ?,
                    tempat_lahir_perempuan = ?,
                    wijk_perempuan = ?,
                    tanggal_pernikahan = ?,
                    pukul_pernikahan = ?
                WHERE id = ?
            """, (
                nama_lengkap_laki,
                nama_ayah_laki,
                nama_ibu_laki,
                tempat_lahir_laki,
                wijk_laki,
                nama_lengkap_perempuan,
                nama_ayah_perempuan,
                nama_ibu_perempuan,
                tempat_lahir_perempuan,
                wijk_perempuan,
                tanggal_pernikahan,
                pukul_pernikahan,
                id
            ))
            db.commit()
            return(redirect(url_for("pernikahan")))
    else:
        return redirect(url_for("index"))

def editmeninggal():
    # Check if the user is logged in and has Admin status
    if "status" in session and session["status"] == "Admin":
        # Get form data
        id = request.form['modal_id']
        nama_lengkap = request.form['modal_nama_lengkap']
        jenis_kelamin = request.form['modal_jenis_kelamin']
        wijk = request.form['modal_wijk']
        tanggal_baptis = request.form['modal_monding']
        cursor.execute("""
            UPDATE meninggal
            SET nama_lengkap = ?,
                jenis_kelamin = ?,
                wijk = ?,
                monding = ?
            WHERE id = ?
        """, (nama_lengkap, jenis_kelamin, wijk, tanggal_baptis, id))
        db.commit()
        return(redirect(url_for("meninggal_dunia")))
    else:
        return redirect(url_for("index"))

def editpelayan():
    # Ensure the user is an admin (check session status)
    if "status" in session and session["status"] == "Admin":
        # Retrieve form data
        id = request.form['modal_id']
        nama_lengkap = request.form['modal_nama_lengkap']
        jenis_kelamin = request.form['modal_jenis_kelamin']
        status_pelayanan = request.form['modal_status_pelayanan']
        jenis_pelayanan = request.form['modal_jenis_pelayanan']
        tanggal_tahbisan = request.form['modal_tanggal_tahbisan']
        
        cursor.execute("""
            UPDATE pelayan
            SET nama_lengkap = ?,
                jenis_kelamin = ?,
                status_pelayanan = ?,
                jenis_pelayanan = ?,
                tanggal_tahbisan = ?
            WHERE id = ?
        """, (nama_lengkap, jenis_kelamin, status_pelayanan, jenis_pelayanan, tanggal_tahbisan, id))
        
        db.commit()
        return(redirect(url_for("data_pelayanan")))
    else:
        return redirect(url_for("index"))

def editrpp():
    if "status" in session and session["status"] == "Admin":
        id = request.form['modal_id']
        nama_lengkap = request.form['modal_nama_lengkap']
        jenis_kelamin = request.form['modal_jenis_kelamin']
        wijk = request.form['modal_wijk']
        tanggal_rpp = request.form['modal_tanggal_rpp']
        alasan = request.form['modal_alasan']
        cursor.execute("""
            UPDATE rpp
            SET nama_lengkap = ?,
                jenis_kelamin = ?,
                wijk = ?,
                tanggal_rpp = ?,
                alasan = ?
            WHERE id = ?
        """, (nama_lengkap, jenis_kelamin, wijk, tanggal_rpp, alasan, id))
        db.commit()
        return(redirect(url_for("rpp")))
    else:
        return redirect(url_for("index"))

def editsidi():
    if "status" in session and session["status"] == "Admin":
        id = request.form['modal_id']
        nama_lengkap = request.form['modal_nama_lengkap']
        jenis_kelamin = request.form['modal_jenis_kelamin']
        wijk = request.form['modal_wijk']
        tempat_lahir = request.form['modal_tempat_lahir']
        tanggal_lahir = request.form['modal_tanggal_lahir']
        tanggal_baptis = request.form['modal_tanggal_baptis']
        tanggal_sidi = request.form['modal_tanggal_sidi']
        
        cursor.execute("""
            UPDATE sidi
            SET nama_lengkap = ?,
                jenis_kelamin = ?,
                wijk = ?,
                tempat_lahir = ?,
                tanggal_lahir = ?,
                tanggal_baptis = ?,
                tanggal_sidi = ?
            WHERE id = ?
        """, (nama_lengkap, jenis_kelamin, wijk, tempat_lahir, tanggal_lahir, tanggal_baptis, tanggal_sidi, id))
        db.commit()
        return redirect(url_for("jemaat_sidi"))
    else:
        return redirect(url_for("index"))

# def search():
#     results = set()
#     if request.method == 'POST':
#         from_day = request.form.get('from_day')
#         from_month = request.form.get('from_month')
#         to_day = request.form.get('to_day')
#         to_month = request.form.get('to_month')
#         user = request.form.get("option")
#         print(user)
#         if user == "keluarga":
#             from_date = datetime.strptime(f"2023-{from_month}-{from_day}", "%Y-%m-%d")
#             to_date = datetime.strptime(f"2023-{to_month}-{to_day}", "%Y-%m-%d")
#             query = """
#                 SELECT *
#                 FROM keluarga
#                 WHERE strftime('%m-%d', tanggal_lahir) BETWEEN ? AND ?
#                 """
#             cursor.execute(query, (from_date.strftime('%m-%d'), to_date.strftime('%m-%d')))
#             results = cursor.fetchall()
#         if user == "user":
#             from_date = datetime.strptime(f"2023-{from_month}-{from_day}", "%Y-%m-%d")
#             to_date = datetime.strptime(f"2023-{to_month}-{to_day}", "%Y-%m-%d")
#             query = """
#                 SELECT *
#                 FROM user
#                 WHERE strftime('%m-%d', tanggal_menikah) BETWEEN ? AND ?
#                 """
#             cursor.execute(query, (from_date.strftime('%m-%d'), to_date.strftime('%m-%d')))
#             results = cursor.fetchall()
#     return render_template('Admin/cari_umur.html', results=results, user=user)

def calculate_years(date):
    today = datetime.today()
    years_passed = today.year - date.year
    if (today.month, today.day) < (date.month, date.day):
        years_passed -= 1
    return years_passed

def search():
    results = []
    user = ""
    if request.method == 'POST':
        from_day = request.form.get('from_day')
        from_month = request.form.get('from_month')
        to_day = request.form.get('to_day')
        to_month = request.form.get('to_month')
        user = request.form.get("option")
        print(user)
        from_date = datetime.strptime(f"2023-{from_month}-{from_day}", "%Y-%m-%d")
        to_date = datetime.strptime(f"2023-{to_month}-{to_day}", "%Y-%m-%d")
        if user == "keluarga":
            query = """
                SELECT *
                FROM keluarga
                WHERE strftime('%m-%d', tanggal_lahir) BETWEEN ? AND ?
                """
            cursor.execute(query, (from_date.strftime('%m-%d'), to_date.strftime('%m-%d')))
            raw_results = cursor.fetchall()
            for row in raw_results:
                age = calculate_years(datetime.strptime(row[6], "%Y-%m-%d"))
                results.append({"nama": row[2], "tanggal_lahir": row[6], "umur": age, "wijk":row[12]})
        if user == "user":
            query = """
                SELECT *
                FROM user
                WHERE strftime('%m-%d', tanggal_menikah) BETWEEN ? AND ?
                """
            cursor.execute(query, (from_date.strftime('%m-%d'), to_date.strftime('%m-%d')))
            raw_results = cursor.fetchall()
            for row in raw_results:
                age = calculate_years(datetime.strptime(row[8], "%Y-%m-%d"))
                results.append({"nama": row[4], "tanggal_lahir": row[8], "umur": age, "wijk":row[6]})
    return render_template('Admin/cari_umur.html', results=results, user=user)

def search_jemaat():
    if session and "status" in session:
        results = None
        with open("data/nama_wjik.txt", "r") as f:
                wijki = f.read().split("\n")
        if request.method == 'POST':
            wijk = request.form.get('wijk')
            registration_number = request.form.get('registration_number')
            name = request.form.get('name')
            other_search = request.form.get('other_search')

            # SQL query based on user input
            query = "SELECT * FROM keluarga WHERE 1=1"
            params = []
            if wijk:
                query += " AND wijk = ?"
                params.append(wijk)
            if registration_number:
                query += " AND registrasi = ?"
                params.append(registration_number)
            if name:
                query += " AND nama LIKE ?"
                params.append(f"%{name}%")
            if other_search:
                query += " AND (nama LIKE ? OR alamat LIKE ? OR status LIKE ? OR jenis_kelamin LIKE ? OR tempat_lahir LIKE ? OR pekerjaan LIKE ? OR pendidikan LIKE ?)"
                params.extend([f"%{other_search}%", f"%{other_search}%", f"%{other_search}%", f"%{other_search}%", f"%{other_search}%", f"%{other_search}%", f"%{other_search}%"])
            print(query)
            print(params)
            cursor.execute(query, params)
            # Execute the query
            results = cursor.fetchall()
        return render_template("Admin/cari _jemaat.html", wijk=wijki, results=results)
    else:
        return redirect(url_for("index"))

def edit_user2():
    id = request.args.get("id")
    username = request.form.get("username_modal")
    password = request.form.get("password_modal")
    cursor.execute("UPDATE user SET username =?, password =? WHERE id =?", (username, password, id))
    db.commit()
    return redirect(url_for("management_user"))

def hapuswijk():
    if session and session["status"] == "Admin":
        nomor = request.args.get("nomor")
        idx = int(nomor) - 1
        with open("data/nama_wjik.txt", "r") as f:
            wijki = f.read().split("\n")
        del wijki[idx]
        tulisan = "\n".join(wijki)
        print(tulisan)
        with open("data/nama_wjik.txt", "w") as f:
            f.write(tulisan)
        return redirect(url_for("ubah_data_jemaat"))

def addwijk():
    if session and session["status"] == "Admin":
        wjik = request.form.get("namawijk")
        with open("data/nama_wjik.txt", "a") as f:
            f.write(f"\n{wjik}")
        return redirect(url_for("ubah_data_jemaat"))
    else:
        return redirect(url_for("index"))

def url_rule_admin():
    app.add_url_rule("/", "index", index)
    app.add_url_rule("/warta_user", "warta_user", warta_user    )
    app.add_url_rule("/login", "login", login)
    app.add_url_rule("/signin", "signin", signin, methods=["post"])
    app.add_url_rule("/adduser", "adduser", adduser, methods=["post"])
    app.add_url_rule("/hapus", "hapus", hapus)
    app.add_url_rule("/dashboard", "dashboard", dashboard)
    app.add_url_rule("/dashboard/management_user", "management_user", management_user)
    app.add_url_rule("/signout", "keluar", keluar)
    app.add_url_rule("/dashboard/ubah_data_jemaat", "ubah_data_jemaat", ubah_data_jemaat)
    app.add_url_rule("/dashboard/ubah_data_jemaat/keluarga", "keluarga", keluarga)
    app.add_url_rule("/dashboard/ubah_data_jemaat/edit_user", "edit_user", edit_user, methods=["post"])
    app.add_url_rule("/dashboard/jemaat_baptis", "jemaat_baptis", baptis)
    app.add_url_rule("/addbaptis", "addbaptis", addbaptis, methods=["post"])
    app.add_url_rule("/deletebaptis", "deletebaptis", deletebaptis)
    app.add_url_rule("/dashboard/jemaat_sidi", "jemaat_sidi", sidi)
    app.add_url_rule("/addsidi", "addsidi", addsidi, methods=["post"])
    app.add_url_rule("/deletesidi", "deletesidi", deletesidi)
    app.add_url_rule("/dashboard/anak_lahir", "anak_lahir", lahir)
    app.add_url_rule("/addlahir", "addlahir", addlahir, methods=["post"])
    app.add_url_rule("/deletelahir", "deletelahir", deletelahir)
    app.add_url_rule("/dashboard/rpp", "rpp", rpp)
    app.add_url_rule("/addrpp", "addrpp", addrpp, methods=["post"])
    app.add_url_rule("/deleterpp", "deleterpp", deleterpp)
    app.add_url_rule("/dashboard/martumpol", "martumpol", martumpol)
    app.add_url_rule("/addmartumpol", "addmartumpol", addmartumpol, methods=["post"])
    app.add_url_rule("/deletemartumpol", "deletemartumpol", deletemartumpol)
    app.add_url_rule("/dashboard/pernikahan", "pernikahan", pernikahan)
    app.add_url_rule("/addpernikahan", "addpernikahan", addpernikahan, methods=["post"])
    app.add_url_rule("/deletepernikahan", "deletepernikahan", deletepernikahan)
    app.add_url_rule("/dashboard/meninggal_dunia", "meninggal_dunia", meninggal_dunia)
    app.add_url_rule("/addmeninggal", "addmeninggal", addmeninggal, methods=["post"])
    app.add_url_rule("/deletemeninggal", "deletemeninggal", deletemeninggal)
    app.add_url_rule("/dashboard/kegiatan_kebaktian", "kegiatan_kebaktian", kegiatan_kebaktian)
    app.add_url_rule("/addkebaktian", "addkebaktian", addkebaktian, methods=["post"])
    app.add_url_rule("/deletekebaktian", "deletekebaktian", deletekebaktian)
    app.add_url_rule("/dashboard/data_pelayan", "data_pelayanan", data_pelayanan)
    app.add_url_rule("/addpelayan", "addpelayan", addpelayanan, methods=["post"])
    app.add_url_rule("/deletepelayan", "deletepelayan", deletepelayanan)
    app.add_url_rule("/dashboard/warta", "warta", warta)
    app.add_url_rule("/addwarta", "addwarta", addwarta, methods=["post"])
    app.add_url_rule("/deletewarta", "deletewarta", deletewarta)
    app.add_url_rule("/dashboard/berita", "berita", berita)
    app.add_url_rule("/dashboard/berita/add", "add_berita_page", add_berita_page)
    app.add_url_rule("/addberita", "addberita", addberita, methods=["post"])
    app.add_url_rule("/deleteberita", "deleteberita", deleteberita)
    app.add_url_rule("/dashboard/bulanann", "pembayaran", pembayaran)
    app.add_url_rule("/verified", "verified", verify_pembayaran)
    app.add_url_rule("/deletebulanan", "deletebulanan", deletebulanan)
    app.add_url_rule("/static/pdf/<filename>", "show_bukti", show_bukti)
    app.add_url_rule("/lihat", "more_info", more_info)
    app.add_url_rule("/verifiedhamauliateon", "verified_hamauliateon", verify_hamauliateon)
    app.add_url_rule("/deletehamauliateon", "deletehamauliateon", deletehamauliateon)
    app.add_url_rule("/dashboard/hamauliateon", "hamauliateon_admin", hamauliateon_admin)
    app.add_url_rule("/dashboard/warta_keuangan", "warta_keuangan", finansial_page)
    app.add_url_rule("/dashboard/warta_keuangan/edit", "warta_keuangan_edit", finansial_edit)
    app.add_url_rule("/dashboard/warta_keuangan/add", "warta_keuangan_add", finansial_data)
    app.add_url_rule("/submit_financial_data", "submit_financial_data", submit_financial_data, methods=["post"])
    app.add_url_rule("/edit_financial_data", "edit_financial_data", edit_financial_data, methods=["post"])
    app.add_url_rule("/editlahir", "editlahir", editlahir, methods=["post"])
    app.add_url_rule("/editbaptis", "editbaptis", editbaptis, methods=["post"])
    app.add_url_rule("/editmartumpol", "editmartumpol", editmartumpol, methods=["post"])
    app.add_url_rule("/editpernikahan", "editpernikahan", editpernikahan, methods=["post"])
    app.add_url_rule("/editmeninggal", "editmeninggal", editmeninggal, methods=["post"])
    app.add_url_rule("/editpelayan", "editpelayan", editpelayan, methods=["post"])
    app.add_url_rule("/editrpp", "editrpp", editrpp, methods=["post"])
    app.add_url_rule("/editsidi", "editsidi", editsidi, methods=["post"])
    app.add_url_rule("/dashboard/search-jemaat", "search-jemaat", search, methods=["post", "get"])
    app.add_url_rule("/dashboard/cari_data_jemaat", "cari_data_jemaat", search_jemaat, methods=["post", "get"])
    app.add_url_rule("/edituser", "edit_user2", edit_user2, methods=["post", "get"])
    app.add_url_rule("/hapuswijk", "hapuswijk", hapuswijk)
    app.add_url_rule("/addwijk", "addwijk", addwijk, methods=["post", "get"])
    app.add_url_rule("/login/admin", "login_admin", login_admin)
    app.add_url_rule("/signin/admin", "signin_admin", signin_admin, methods=["post", "get"])
    app.add_url_rule("//dashboard/bulanann/add", "addbulanan_admin", addbulanan_admin, methods=["post"])

#ini untuk user
def profile():
    if "nama" in session:
        nama = session["nama"]
        username = session["username"]
        tanggal = session["tanggal_registrasi"]
        id = session["id"]
        command = f"SELECT * FROM keluarga WHERE myid={id}"
        cursor.execute(command)
        keluarga = cursor.fetchall()
        total_keluarga = len(keluarga)
        tanggungan = 0
        for i in keluarga:
            if i[3] == "tanggungan":
                tanggungan += 1
        command = f"SELECT * FROM pelayanan WHERE nama_lengkap='{nama}'"
        cursor.execute(command)
        pelayanan = cursor.fetchall()
        jumlah_pelayanan = len(pelayanan)
        command = f"SELECT * FROM bulanan WHERE username='{username}'"
        cursor.execute(command)
        bulanan = cursor.fetchall()
        nominal = 0
        for i in bulanan:
            if i[6] == "verified":
                nominal += int(i[3])
        username = session["username"]
        command = f"SELECT * FROM hamauliateon WHERE username='{username}'"
        cursor.execute(command)
        bulanan = cursor.fetchall()
        hamauliateon = 0
        count = len(bulanan)
        # print(len(bulanan))
        if count > 0:
            for i in bulanan:
                if i[19] == "verified":
                    hamauliateon += int(i[17])
        str_nominal = locale.currency(nominal, grouping=True)[:-3]
        str_hamauliateon = locale.currency(hamauliateon, grouping=True)[:-3]
        return render_template("User/profile.html", 
                               nama=nama, 
                               tanggal=tanggal, 
                               jumlah_keluarga=total_keluarga, 
                               jumlah_pelayanan=jumlah_pelayanan,
                               jumlah_bulanan = str_nominal,
                               tanggungan = tanggungan,
                               hamauliateon= str_hamauliateon)
    
def user_keluarga():
    if "nama" in session:
        # with open("data/nama_wjik.txt", "r") as f:
        #     wijk = f.read().split("\n")
        id = session["id"]
        command = f"SELECT * FROM user WHERE id={id}"
        cursor.execute(command)
        user = cursor.fetchone()
        command = f"SELECT * FROM keluarga WHERE myid={id}"
        query = request.args.get("query")
        if query:
            command += f" AND nama LIKE '%{query}%' OR status LIKE '%{query}%'"
        cursor.execute(command)
        keluarga = cursor.fetchall()
        return render_template("User/keluarga.html", user=user, families=keluarga)

def addkeluarga():
    id = session["id"]
    nama = request.form.get("nama")
    status = request.form.get("status")
    jenis_kelamin = request.form.get("jenis_kelamin")
    tempat_lahir = request.form.get("tempat_lahir")
    tanggal_lahir = request.form.get("tanggal_lahir")
    tanggal_baptis = request.form.get("tanggal_baptis")
    tanggal_sidi = request.form.get("tanggal_sidi")
    pekerjaan = request.form.get("pekerjaan")
    pendidikan = request.form.get("pendidikan")
    alamat = session["alamat"]
    wijk = session["wijk"]
    registrasi = session["registrasi"]
    command = f"INSERT INTO keluarga(myid, nama, status, jenis_kelamin, tempat_lahir, tanggal_lahir, tanggal_baptis, tanggal_sidi, pekerjaan, pendidikan, alamat, wijk, registrasi) VALUES({id}, '{nama}', '{status}', '{jenis_kelamin}', '{tempat_lahir}', '{tanggal_lahir}', '{tanggal_baptis}', '{tanggal_sidi}', '{pekerjaan}', '{pendidikan}', '{alamat}', '{wijk}', '{registrasi}')"
    cursor.execute(command)
    db.commit()
    return redirect(url_for("user_keluarga"))

def editkeluarga():
    id = request.form.get("modal_id")
    nama = request.form.get("modal_nama")
    status = request.form.get("modal_status")
    jenis_kelamin = request.form.get("modal_jenis_kelamin")
    tempat_lahir = request.form.get("modal_tempat_lahir")
    tanggal_lahir = request.form.get("modal_tanggal_lahir")
    tanggal_baptis = request.form.get("modal_tanggal_baptis")
    tanggal_sidi = request.form.get("modal_tanggal_sidi")
    pekerjaan = request.form.get("modal_pekerjaan")
    pendidikan = request.form.get("modal_pendidikan")
    #sql edit data in keluarga
    command = f"UPDATE keluarga SET nama='{nama}', status='{status}', jenis_kelamin='{jenis_kelamin}', tempat_lahir='{tempat_lahir}', tanggal_lahir='{tanggal_lahir}', tanggal_baptis='{tanggal_baptis}', tanggal_sidi='{tanggal_sidi}', pekerjaan='{pekerjaan}', pendidikan='{pendidikan}' WHERE id={id}"
    cursor.execute(command)
    db.commit()
    return redirect(url_for("user_keluarga"))

def deletekeluarga():
    myid = session["id"]
    id = request.args.get("id")
    print(myid)
    print(id)
    command = f"DELETE FROM keluarga WHERE id={id} AND myid={myid}"
    cursor.execute(command)
    db.commit()
    return redirect(url_for("user_keluarga"))

def pelayanan_user():
    if "nama" in session:
        return render_template("User/layanan.html")

def bulanan_user():
    if "nama" in session:
        username = session["username"]
        command = f"SELECT * FROM bulanan WHERE username='{username}'"
        nama = session["nama"]
        cursor.execute(command)
        bulanan = cursor.fetchall()
        nominal = 0
        pending = 0
        count = 0
        # print(len(bulanan))
        if len(bulanan) > 0:
            for i in bulanan:
                if i[6] == "verified":
                    nominal += int(i[3])
                    count += 1
                else:
                    pending += 1
        str_nominal = locale.currency(nominal, grouping=True)[:-3]
        return render_template("User/bulanan.html", nominal=str_nominal, pending=pending, count=count, nama=nama)

def addbulanan():
    if "status" in session:
        username = session["username"]
        nama_keluarga = request.form.get('nama')
        nominal_persembahan = request.form.get('nominal')
        persembahan_bulan = request.form.get('bulan')
        bukti_persembahan = request.files.get('bukti')
        file_path = None
        if bukti_persembahan:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], bukti_persembahan.filename)
            bukti_persembahan.save(file_path)
        command = f"INSERT INTO bulanan (username, nama, nominal, bulan, bukti, status) VALUES ('{username}', '{nama_keluarga}', {nominal_persembahan}, '{persembahan_bulan}', '{file_path}', 'pending') "
        cursor.execute(command)
        db.commit()
        return redirect(url_for("bulanan_user"))

def hamauliateon_user():
    if "nama" in session:
        username = session["username"]
        nama = session["nama"]
        myid = session["id"]
        command = f"SELECT * FROM keluarga WHERE myid = {myid}"
        cursor.execute(command)
        keluarga = cursor.fetchall()
        command = f"SELECT * FROM hamauliateon WHERE username='{username}'"
        cursor.execute(command)
        bulanan = cursor.fetchall()
        nominal = 0
        pending = 0
        count = len(bulanan)
        # print(len(bulanan))
        if count > 0:
            for i in bulanan:
                if i[19] == "verified":
                    nominal += int(i[17])
                else:
                    pending += 1
        str_nominal = locale.currency(nominal, grouping=True)[:-3]
        return render_template("User/hamauliateon.html", nominal=str_nominal, pending=pending, keluarga=keluarga, nama=nama)

def addhamauliateon():
    if "status" in session:
        username = session["username"]
        nama_keluarga = request.form.get('nama_keluarga')
        nama = request.form.get("nama")
        huria = request.form.get("huria") or 0
        pembangunan = request.form.get("pembangunan") or 0
        diakonia = request.form.get("diakonia") or 0
        pendeta = request.form.get("pendeta") or 0
        sintua = request.form.get("sintua") or 0
        perhalado = request.form.get("parhalado") or 0
        ama = request.form.get("ama") or 0
        ina = request.form.get("ina") or 0
        nhkbp = request.form.get("nhkbp") or 0
        remaja = request.form.get("remaja") or 0
        sekolah_minggu = request.form.get("sekolah_minggu") or 0
        pemusik = request.form.get("pemusik") or 0
        multimedia = request.form.get("multimedia") or 0
        song_leader = request.form.get("song_leader") or 0
        total = int(huria) + int(pembangunan) + int(diakonia) + int(pendeta) + int(sintua) + int(perhalado) + int(ama) + int(ina) + int(nhkbp) + int(remaja) + int(sekolah_minggu) + int(pemusik) + int(multimedia) + int(song_leader)
        status = "pending"
        bukti_persembahan = request.files.get('bukti')
        file_path = None
        if bukti_persembahan:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], bukti_persembahan.filename)
            bukti_persembahan.save(file_path)
        command = f"INSERT INTO hamauliateon (username, nama, huria, pembangunan, diakonia, pendeta, sintua, perhalado, ama, ina, nhkbp, remaja, sekolah_minggu, pemusik, multimedia, song_leader, total, status, bukti, nama_keluarga) VALUES ('{username}', '{nama}', {huria}, {pembangunan}, {diakonia}, {pendeta}, {sintua}, {perhalado}, {ama}, {ina}, {nhkbp}, {remaja}, {sekolah_minggu}, {pemusik}, {multimedia}, {song_leader}, {total}, '{status}', '{file_path}', '{nama_keluarga}')"
        cursor.execute(command)
        db.commit()
        return redirect(url_for("hamauliateon_user"))

def user_anaklahir():
    with open("data/nama_wjik.txt", "r") as f:
        wijk = f.read().split("\n")
    if "nama" in session:
        return render_template("User/add_anaklahir.html", wijk=wijk)
    else:
        return redirect(url_for("profile"))

def user_baptis():
    if "nama" in session:
        with open("data/nama_wjik.txt", "r") as f:
            wijk = f.read().split("\n")
        return render_template("User/add_baptis.html", wijk=wijk)
    else:
        return redirect(url_for("profile"))
    
def user_martumpol():
    if "nama" in session:
        with open("data/nama_wjik.txt", "r") as f:
            wijk = f.read().split("\n")
        return render_template("User/add_martumpol.html", wijk=wijk)
    else:
        return redirect(url_for("profile"))

def user_pernikahan():
    if "nama" in session:
        with open("data/nama_wjik.txt", "r") as f:
            wijk = f.read().split("\n")
        return render_template("User/add_pernikahan.html", wijk=wijk)
    else:
        return redirect(url_for("profile"))

def user_sidi():
    if "nama" in session:
        with open("data/nama_wjik.txt", "r") as f:
            wijk = f.read().split("\n")
        return render_template("User/add_sidi.html", wijk=wijk)
    else:
        return redirect(url_for("profile"))

def user_berita():
    i = request.args.get("index")
    i = int(i) - 1
    with open("data/berita.json", "r") as f:
        data = json.load(f)
    news = data[i]
    return render_template("User/berita.html", user=news)

def koikonia():
    logged = ""
    if session:
        logged = session["status"]
    return render_template("Koinonia.html", logged=logged)
def diakonia():
    logged = ""
    if session:
        logged = session["status"]
    return render_template("Diakonia.html", logged=logged)
def marturia():
    logged = ""
    if session:
        logged = session["status"]
    return render_template("Marturia.html", logged=logged)
def organisasi():
    logged = ""
    if session:
        logged = session["status"]
    return render_template("Organisasi.html", logged=logged)

def url_rule_user():
    app.add_url_rule("/profile", "profile", profile)
    app.add_url_rule("/profile/keluarga", "user_keluarga", user_keluarga)
    app.add_url_rule("/editkeluarga", "editkeluarga", editkeluarga, methods=["post"])
    app.add_url_rule("/addkeluarga", "addkeluarga", addkeluarga, methods=["post"])
    app.add_url_rule("/deletekeluarga", "deletekeluarga", deletekeluarga)
    app.add_url_rule("/profile/layanan", "pelayanan_user", pelayanan_user)
    app.add_url_rule("/profile/bulanan", "bulanan_user", bulanan_user)
    app.add_url_rule("/addbulanan", "addbulanan", addbulanan, methods=["post"])
    app.add_url_rule("/profile/hamauliateon", "hamauliateon_user", hamauliateon_user)
    app.add_url_rule("/addhamauliateon", "addhamauliateon", addhamauliateon, methods=["post"])
    app.add_url_rule("/profile/anak_lahir", "user_anaklahir", user_anaklahir)
    app.add_url_rule("/profile/jemaat_baptis", "user_baptis", user_baptis)
    app.add_url_rule("/profile/martumpal", "user_martumpal", user_martumpol)
    app.add_url_rule("/profile/pernikahan", "user_pernikahan", user_pernikahan)
    app.add_url_rule("/profile/jemaat_sidi", "user_sidi", user_sidi)
    app.add_url_rule("/berita", "user_berita", user_berita)
    app.add_url_rule("/koinonia", "koikonia", koikonia)
    app.add_url_rule("/diakonia", "diakonia", diakonia)
    app.add_url_rule("/marturia", "marturia", marturia)
    app.add_url_rule("/organisasi", "organisasi", organisasi)

url_rule_admin()
url_rule_user()

if __name__ == '__main__':
    app.run(debug=True)
 
 