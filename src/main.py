import tkinter as tk

def main():
  root = tk.Tk()
  root.title("Wavelength")

  button = tk.Button(root,command=lambda:print("button works"))
  button.pack()
  
  root.mainloop()

if __name__ == "__main__":
  main()
