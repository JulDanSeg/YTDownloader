import yt_dlp
from tkinter import *
from tkinter import ttk
import os

from pathlib import Path
ruta_descargas = str(Path.home() / "Downloads")

#root
root=Tk()
root.resizable(True,True)
root.config(bg="#1f618d")
root.title("YTDOWNLOADER")


#MARCO
marco=Frame(root,bg="#1f618d",width="950",height="950")
marco.pack(fill="both",expand=True)
titulo=Label(marco,text="YT DOWNLOADER")
titulo.grid(row=0,column=0,columnspan=4,pady=15,padx=15)
titulo.config(bg="#1f618d",width=40,font=("Rockwell",16,"bold"),anchor="center")



#ETIQUETAS - INGRESO DE DATOS
labnom=Label(marco,text="URL ")
labnom.grid(row=1,column=0,sticky="e",pady=15,padx=15)
labnom.config(bg="#1f618d", font=("Arial", 12, "bold"))

labape=Label(marco,text="FORMATO ")
labape.grid(row=2,column=1,sticky=" ",pady=15,padx=15)
labape.config(bg="#1f618d", font=("Arial", 12, "bold"))

#variables
enlace = StringVar() 

seleccion_Audio_o_Video= StringVar(value='ambos')


ext = StringVar()
height = StringVar()

#ENTRYS
txtnom=Entry(marco, textvariable=enlace)
txtnom.grid(row=1,column=1,sticky=" ",pady=15,padx=15)
txtnom.config(state="normal", bg="white", width=50)


#RADIOBUTTONS
rbvid=Radiobutton(marco, text='Solo video', variable=seleccion_Audio_o_Video, value='video')
rbvid.grid(row=3,column=0,sticky=" ",pady=15,padx=15)


rbaud=Radiobutton(marco, text='Solo Audio', variable=seleccion_Audio_o_Video, value='audio')
rbaud.grid(row=3,column=1,sticky=" ",pady=15,padx=15)


txtape=Radiobutton(marco, text='Audio y Video', variable=seleccion_Audio_o_Video, value='ambos')
txtape.grid(row=3,column=2,sticky=" ",pady=15,padx=15)



#ejecucion
def my_hook(d):
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
        if total_bytes:
            porcentaje = d['downloaded_bytes'] / total_bytes * 100
            barra_progreso['value'] = porcentaje
            estado_label.config(text="Descargando...")
            root.update_idletasks()  # actualiza la GUI
    elif d['status'] == 'finished':
        barra_progreso['value'] = 100
        estado_label.config(text="¡Descarga completa!")
        root.update_idletasks()


def descarga():
    url = enlace.get()
    #comprobaciones
    if seleccion_Audio_o_Video == 'video':
        Audio_o_video = 'bestvideo'
    elif seleccion_Audio_o_Video == 'audio':
        Audio_o_video = 'bestaudio'
    elif seleccion_Audio_o_Video == 'ambos':
        Audio_o_video = 'best'
    else:
        Audio_o_video ='best'

    ydl_opts = {
    'format': f'{Audio_o_video}/best',
    'outtmpl': '%(title)s.%(ext)s',
    'paths': {'home': ruta_descargas},
    'quiet': False,
    'progress_hooks' : [my_hook]
}
    
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

botondescarga=Button(marco,text="DESCARGAR", relief="groove", command=lambda:descarga())
botondescarga.grid(row=6,column=1, padx=10, pady=10)
botondescarga.config(bg="lightgreen", width=10, font=("Arial", 11, "bold"))

barra_progreso = ttk.Progressbar(marco, orient='horizontal', mode='determinate', length=400)
barra_progreso.grid(row=7, column=0, columnspan=3, pady=20)

estado_label = Label(marco, text="", bg="#1f618d", font=("Arial", 12, "bold"), fg="white")
estado_label.grid(row=8, column=0, columnspan=3, pady=10)



root.mainloop()