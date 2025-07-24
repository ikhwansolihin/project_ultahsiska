import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Harga sewa per jam untuk setiap tipe PS
HARGA_PER_JAM = {
    "PS3": 5000,
    "PS4": 7000,
    "PS5": 10000
}

# Fungsi untuk menghitung total dan menampilkan struk
def hitung_total():
    nama = entry_nama.get()
    ps_type = var_ps.get()
    jam = entry_jam.get()

    if not nama or not jam:
        messagebox.showerror("Error", "Semua field harus diisi!")
        return

    try:
        jam = int(jam)
    except ValueError:
        messagebox.showerror("Error", "Jam harus berupa angka!")
        return

    harga = HARGA_PER_JAM[ps_type]
    total = harga * jam

    waktu_sekarang = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Tampilkan hasil
    struk = f"""
    ====== STRUK RENTAL PS ======
    Tanggal & Waktu : {waktu_sekarang}
    Nama Pelanggan  : {nama}
    Tipe PS         : {ps_type}
    Durasi          : {jam} jam
    Harga per Jam   : Rp {harga:,}
    -----------------------------
    Total Bayar     : Rp {total:,}
    =============================
    """
    text_output.config(state='normal')
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, struk)
    text_output.config(state='disabled')

# GUI Setup
root = tk.Tk()
root.title("Elba Playstation - Millenia Group")
root.geometry("420x470")
root.resizable(False, False)

# Form Input
tk.Label(root, text="Nama Pelanggan").pack(pady=5)
entry_nama = tk.Entry(root, width=40)
entry_nama.pack()

tk.Label(root, text="Pilih Tipe PS").pack(pady=5)
var_ps = tk.StringVar(value="PS3")
tk.OptionMenu(root, var_ps, *HARGA_PER_JAM.keys()).pack()

tk.Label(root, text="Durasi (jam)").pack(pady=5)
entry_jam = tk.Entry(root, width=20)
entry_jam.pack()

# Tombol Hitung
tk.Button(root, text="Hitung Total", command=hitung_total, bg="blue", fg="white").pack(pady=10)

# Output Struk
tk.Label(root, text="Struk Pembayaran").pack(pady=5)
text_output = tk.Text(root, height=13, width=50, state='disabled')
text_output.pack(pady=5)

# Jalankan GUI
root.mainloop()
