import tkinter as tk
import pyshorteners
from tkinter import font as tkfont
def short_url():
    url = long_url_entry.get()
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)
    short_url_entry.configure(state='normal')
    short_url_entry.delete(0, tk.END)
    short_url_entry.insert(0, short_url)
    short_url_entry.configure(state='readonly')
    print(short_url)

#defining the main window
root = tk.Tk()
root.title("URL Shortener")
root.geometry("500x250")
root.configure(bg ='#f7f7f7')

#Adding font 
fontStyle = tkfont.Font(family="Lucida Grande", size=10)

#adding frames 
top_frame = tk.Frame(root, bg='#f7f7f7')
top_frame.pack(side='top')
bottom_frame = tk.Frame(root, bg='#f7f7f7')
bottom_frame.pack(side='top')


#long url label
long_url_label = tk.Label(top_frame, text="Enter the Long URL: ", font=fontStyle, bg='#f7f7f7')
long_url_entry = tk.Entry(top_frame, width=50,font =fontStyle) #entry widget to get the long url
long_url_label.pack(side='top',padx=10, pady=20)
long_url_entry.pack(side='top', pady=10)

#short url label
short_url_label = tk.Label(bottom_frame, text="Short URL: ", font=fontStyle, bg='#f7f7f7')
short_url_entry = tk.Entry(bottom_frame, width=40,font=fontStyle,state='readonly') #entry widget to display the short url
short_url_label.pack(side='top',padx=10, pady=20)
short_url_entry.pack(side='top', pady=10)

#short url button
button = tk.Button(bottom_frame, text="Shorten URL", command=short_url, font=fontStyle, bg='#f7f7f7')
button.pack(padx=5, pady=5)

# #defining a function to shorten the url



# #defining a function to shorten the url
# def short_url():
root.mainloop()