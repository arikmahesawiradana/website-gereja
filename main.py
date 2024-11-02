from flask import *
import sqlite3
import json
import os
from datetime import datetime

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
    pendidikan TEXT
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

def warta_user():
    with open("data/warta_jemaat.json", "r") as f:
        data = json.load(f)
    return render_template("User/warta.html", data=data)

def login():
    error = request.args.get("error") or ""
    return render_template("User/login.html", error=error)

def signin():
    username = request.form.get("username")
    password = request.form.get("password")
    print(username)
    print(password)
    if username == "Admin" and password == "Admin":
        session["username"] = username
        session["password"] = password
        session["status"] = "Admin"
        return redirect(url_for("dashboard"))
    else:
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
        if "status" in session:
            page = request.args.get("page") or ""
            return render_template("Admin/dashboard.html", page=page)
    else:
        return redirect(url_for("index"))

def management_user():
    if "status" in session:
        command = "SELECT * FROM user"
        cursor.execute(command)
        users = cursor.fetchall()
        return render_template("Admin/management_user.html", users=users)
    else:
        return redirect(url_for("index"))

def adduser():
    if "status" in session:
        username = request.form.get("username")
        password = request.form.get("password")
        status = "Peserta"
        command = f"INSERT INTO user(username, password, status) VALUES('{username}', '{password}', '{status}')"
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
        if "status" in session:
            with open("data/nama_wjik.txt", "r") as f:
                wjik = f.read().split("\n")
            print(wjik)
            command = "SELECT * FROM user"
            cursor.execute(command)
            users = cursor.fetchall()
            return render_template("Admin/ubah_data_jemaat.html", users=users, wjik=wjik)
    else:
        return redirect(url_for("index"))

def keluarga():
    if "status" in session:
        if "status" in session:
            with open("data/nama_wjik.txt", "r") as f:
                wijk = f.read().split("\n")
            id = request.args.get("id")
            command = f"SELECT * FROM user WHERE id={id}"
            cursor.execute(command)
            user = cursor.fetchone()
            command = f"SELECT * FROM keluarga WHERE myid={id}"
            cursor.execute(command)
            keluarga = cursor.fetchall()
            return render_template("Admin/data_keluarga.html", user=user, wijk=wijk, families=keluarga)
    else:
        return redirect(url_for("index"))

def edit_user():
    if "status" in session:
        if "status" in session:
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
        if "status" in session:
            with open("data/nama_wjik.txt", "r") as f:
                wijk = f.read().split("\n")
            command = "SELECT * FROM baptis"
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
            return redirect(url_for("jemaat_baptis"))

def deletebaptis():
    id = request.args.get("id")
    command = f"DELETE FROM baptis WHERE id={id}"
    cursor.execute(command)
    db.commit()
    return redirect(url_for("jemaat_baptis"))

def sidi():
    if "status" in session:
        if "status" in session:
            with open("data/nama_wjik.txt", "r") as f:
                wijk = f.read().split("\n")
            command = "SELECT * FROM sidi"
            cursor.execute(command)
            users = cursor.fetchall()
            return render_template("Admin/sidi.html", users=users, wijk=wijk)
    else:
        return redirect(url_for("index"))

def addsidi():
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
            return redirect(url_for("jemaat_sidi"))

def deletesidi():
    id = request.args.get("id")
    command = f"DELETE FROM sidi WHERE id={id}"
    cursor.execute(command)
    db.commit()
    return redirect(url_for("jemaat_sidi"))

def lahir():
    if "status" in session:
        if "status" in session:
            with open("data/nama_wjik.txt", "r") as f:
                wijk = f.read().split("\n")
            command = "SELECT * FROM anak_lahir"
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
            return redirect(url_for("anak_lahir"))

def deletelahir():
    id = request.args.get("id")
    command = f"DELETE FROM anak_lahir WHERE id={id}"
    cursor.execute(command)
    db.commit()
    return redirect(url_for("anak_lahir"))

def rpp():
    if "status" in session:
        if "status" in session:
            with open("data/nama_wjik.txt", "r") as f:
                wijk = f.read().split("\n")
            command = "SELECT * FROM rpp"
            cursor.execute(command)
            users = cursor.fetchall()
            return render_template("Admin/rpp.html", users=users, wijk=wijk)
    else:
        return redirect(url_for("index"))

def addrpp():
    if "status" in session:
            nama_lengkap = request.form.get("nama_lengkap")
            jenis_kelamin = request.form.get("jenis_kelamin")
            tanggal_rpp = request.form.get("tanggal_rpp")
            alasan = request.form.get("alasan")
            wijk = request.form.get("wijk")
            command = f"INSERT INTO rpp(nama_lengkap, jenis_kelamin, wijk, tanggal_rpp, alasan) VALUES('{nama_lengkap}', '{jenis_kelamin}', '{wijk}', '{tanggal_rpp}', '{alasan}')"
            cursor.execute(command)
            db.commit()
            return redirect(url_for("rpp"))

def deleterpp():
    id = request.args.get("id")
    command = f"DELETE FROM rpp WHERE id={id}"
    cursor.execute(command)
    db.commit()
    return redirect(url_for("rpp"))

def martumpol():
    if "status" in session:
        if "status" in session:
            with open("data/nama_wjik.txt", "r") as f:
                wijk = f.read().split("\n")
            command = "SELECT * FROM martumpol"
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
            return redirect(url_for("martumpol"))

def deletemartumpol():
    id = request.args.get("id")
    command = f"DELETE FROM martumpol WHERE id={id}"
    cursor.execute(command)
    db.commit()
    return redirect(url_for("martumpol"))

def pernikahan():
    if "status" in session:
        if "status" in session:
            with open("data/nama_wjik.txt", "r") as f:
                wijk = f.read().split("\n")
            command = "SELECT * FROM pernikahan"
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
            return redirect(url_for("pernikahan"))

def deletepernikahan():
    id = request.args.get("id")
    command = f"DELETE FROM pernikahan WHERE id={id}"
    cursor.execute(command)
    db.commit()
    return redirect(url_for("pernikahan"))

def meninggal_dunia():
    if "status" in  session:
        if "status" in session:
            with open("data/nama_wjik.txt", "r") as f:
                wijk = f.read().split("\n")
            command = "SELECT * FROM meninggal"
            cursor.execute(command)
            users = cursor.fetchall()
            return render_template("Admin/meninggal_dunia.html", users=users, wijk=wijk)
    else:
        return redirect(url_for("index"))

def addmeninggal():
    if "status" in session:
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
    id = request.args.get("id")
    command = f"DELETE FROM meninggal WHERE id={id}"
    cursor.execute(command)
    db.commit()
    return redirect(url_for("meninggal_dunia"))

def kegiatan_kebaktian():
    if "status" in session:
        if "status" in session:
            command = "SELECT * FROM kebaktian"
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
    id = request.args.get("id")
    command = f"DELETE FROM kebaktian WHERE id={id}"
    cursor.execute(command)
    db.commit()
    return redirect(url_for("kegiatan_kebaktian"))

def data_pelayanan():
    if "status" in session:
        if "status" in session:
            with open("data/nama_wjik.txt", "r") as f:
                wijk = f.read().split("\n")
            command = "SELECT * FROM pelayanan"
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
    id = request.args.get("id")
    command = f"DELETE FROM pelayanan WHERE id={id}"
    cursor.execute(command)
    db.commit()
    return redirect(url_for("data_pelayanan"))

def warta():
    if "status" in session:
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
    myid = request.args.get("id")
    myid = int(myid) - 1
    with open("data/warta_jemaat.json", "r") as fil:
        data = json.load(fil)
    data_remove = data[myid]
    data.remove(data_remove)
    with open("data/warta_jemaat.json", "w") as fil:
        json.dump(data, fil)
    return redirect(url_for("warta"))

def berita():
    if "status" in session:
        with open("data/berita.json", "r") as file:
            data = json.load(file)
        return render_template("Admin/berita.html", data=data)
    else:
        return redirect(url_for("login"))
    
def add_berita_page():
    if "status" in session:
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
    myid = request.args.get("id")
    myid = int(myid) - 1
    with open("data/berita.json", "r") as fil:
        data = json.load(fil)
    data_remove = data[myid]
    data.remove(data_remove)
    with open("data/berita.json", "w") as fil:
        json.dump(data, fil)
    return redirect(url_for("warta"))

def pembayaran():
    if "status" in session:
        command = f"SELECT * FROM bulanan"
        cursor.execute(command)
        users = cursor.fetchall()
        return render_template("Admin/bulanan.html", users=users)
    
def verify_pembayaran():
    id = request.args.get("id")
    #create sql command set status into verified where id is from variable call id
    command = f"UPDATE bulanan SET status='verified' WHERE id={id}"
    cursor.execute(command)
    db.commit()
    return redirect(url_for("pembayaran"))

def more_info():
    id = request.args.get("id")
    page = request.args.get("page")
    command = f"SELECT * FROM {page} WHERE id={id}"
    cursor.execute(command)
    user = cursor.fetchone()
    print(user)
    return render_template("more_info.html", user=user, page=page)

def show_bukti(filename):
    image_path = os.path.join(app.static_folder, 'pdf', filename)
    if not os.path.isfile(image_path):
        # Jika tidak ada, tampilkan error 404
        abort(404)
    print(f"pdf/{filename}")
    return render_template("Admin/bukti.html", filename=f"pdf/{filename}")

def deletebulanan():
    id = request.args.get("id")
    command = f"DELETE FROM bulanan WHERE id={id}"
    cursor.execute(command)
    db.commit()
    return redirect(url_for("pembayaran"))


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
    app.add_url_rule("/dashboard/martumpal", "martumpol", martumpol)
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

#ini untuk user
def profile():
    if "nama" in session:
        nama = session["nama"]
        tanggal = session["tanggal_registrasi"]
        return render_template("User/profile.html", nama=nama, tanggal=tanggal)
    
def user_keluarga():
    if "nama" in session:
        # with open("data/nama_wjik.txt", "r") as f:
        #     wijk = f.read().split("\n")
        id = session["id"]
        command = f"SELECT * FROM user WHERE id={id}"
        cursor.execute(command)
        user = cursor.fetchone()
        command = f"SELECT * FROM keluarga WHERE myid={id}"
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
    #add all of those data into database keluarga
    command = f"INSERT INTO keluarga(myid, nama, status, jenis_kelamin, tempat_lahir, tanggal_lahir, tanggal_baptis, tanggal_sidi, pekerjaan, pendidikan) VALUES({id}, '{nama}', '{status}', '{jenis_kelamin}', '{tempat_lahir}', '{tanggal_lahir}', '{tanggal_baptis}', '{tanggal_sidi}', '{pekerjaan}', '{pendidikan}')"
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
        cursor.execute(command)
        bulanan = cursor.fetchall()
        nominal = 0
        pending = 0
        count = len(bulanan)
        # print(len(bulanan))
        if count > 0:
            for i in bulanan:
                if i[6] == "verified":
                    nominal += int(i[3])
                else:
                    pending += 1
        return render_template("User/bulanan.html", nominal=nominal, pending=pending, count=count)

def addbulanan():
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

def url_rule_user():
    app.add_url_rule("/profile", "profile", profile)
    app.add_url_rule("/profile/keluarga", "user_keluarga", user_keluarga)
    app.add_url_rule("/addkeluarga", "addkeluarga", addkeluarga, methods=["post"])
    app.add_url_rule("/deletekeluarga", "deletekeluarga", deletekeluarga)
    app.add_url_rule("/profile/layanan", "pelayanan_user", pelayanan_user)
    app.add_url_rule("/profile/persembahan", "bulanan_user", bulanan_user)
    app.add_url_rule("/addbulanan", "addbulanan", addbulanan, methods=["post"])


url_rule_admin()
url_rule_user()

if __name__ == '__main__':
    app.run(debug=True)
 