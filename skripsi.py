#Memanggil library
import tkinter as tk
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report

#load model vgg.h5
#modelvgg = load_model("vgg16.h5")
#modelalexnet = load_model("alexnet.h5")
modelmobilenet = load_model("model_mb_v1_final.h5")

#Membuat label untuk klasifikasi
classes = {
 0: 'Pakaian Adat Jawa Yogyakarta',
 1: 'Pakaian Adat Jawa Solo'
}

#inisialisasi GUI
layar = tk.Tk()
#Judul Title pada Tab
layar.title('Identifikasi Pakaian Adat Jawa Yogayakrta \n Dan \n Pakaian Adat Jawa Solo')
#Ukuran
layar.geometry('500x250')
layar.cofigure(background="white")

#Membuat heading pada GUI
heading = Label(layar, text = "Identifikasi Pakaian Adat Jawa Yogayakrta \n Dan \n Pakaian Adat Jawa Solo",pady=20, font=('arial', 20, 'bold'))
heading.configure(background="white", foreground='black')
heading.pack()

#Membuat tombol untuk Upload gambar
upload = Button(layar, text="Pilih",command=upload_image, padx=10, pady=5)
upload.configure(background="#800000", foreground='white',font=('arial', 10, 'bold'))
upload.pack(side='BOTTOM', padx=0.01, pady=10)

#fungsi tombol klasifikasi
def cbutton(file_path):
    class_button = Button(layar, text="Identifikasi Pakaian Adat Jawa Yogayakrta \n Dan \n Pakaian Adat Jawa Solo",
                          command=lambda: classify(file_path), padx=10, pad=5)
    class_button.configure(background="#800000", foreground="white", font=('arial', 10, 'bold'))
    class_button.place(relx=0.01, rely=0.44)


#Membuat fungsi upload gambar
def upload_image():
    file_path = filedialog.askopenfilename()
    uploaded = PIL.Image.open(file_path)
    uploaded.thumbnail(((top.winfo_width()/2.25), (top.winfo_height()/2.25)))
    im = ImageTk.PhotoImage(uploaded)
    sign_image.configure(image=im)
    sign_image.image = im
    layar.configure(text=' ')
    show_classify_button(file_path)


#membuat fungsi untuk klasifikasi dan identifikasi    
def classify(file_path):
    path = file_path

    img = tf.io.read_file(path)
    img = tf.image.decode_jpeg(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = tf.image.resize(img, [224, 224])

    image_input = tf.expand_dims(img, 0)
    identification = layar.predict(image_input)
    class_namses = classes.values()
    class_nam = list(class_namses)
    cek = class_nam[np.argmax(identification)]
    layar.configure(foreground='#011638', text=cek)
    print()
    print("="*100)
    print(identification)
    print("\nData Citra Tersebut termasuk dalam {} dengan tingkat keakuratan {:.2f} persen.".format(class_nam[np.argmax(identification)], 100 * np.max(identification)))
        
    #menjalankan GUI
    layar.mainloop()