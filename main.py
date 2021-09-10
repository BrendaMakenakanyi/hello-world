from tkinter.constants import NW
from PIL import ImageTk,Image
from collections import deque
import tkinter as tk
from tkinter import messagebox
import button

class Main:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("SUN CAFE")
        self.window.geometry("610x497")
        self.canvas = tk.Canvas(
                      self.window,
                      bg = "#FFFFFF",
                      height = 697,
                      width = 867,
                      relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        # paths of the customer images
        self.images = [
              "/home/makena/Desktop/Restaurant/customers/c1.jpeg",
              "/home/makena/Desktop/Restaurant/customers/c2.jpeg",
              "/home/makena/Desktop/Restaurant/customers/c3.jpeg",
              "/home/makena/Desktop/Restaurant/customers/c4.jpeg",
              "/home/makena/Desktop/Restaurant/customers/c5.jpeg",
              "/home/makena/Desktop/Restaurant/customers/c6.jpeg",
              "/home/makena/Desktop/Restaurant/customers/c7.jpeg",
              "/home/makena/Desktop/Restaurant/customers/c8.jpeg"
            ]
        self.img=[]
        self.text=deque()
        self.labels=deque()
        
        
        # Buttons Start
        self.addFirst = button.Button("Add First", 50, 330, self.addFirst)
        self.removeFirst = button.Button("Remove First", 50, 390, self.removeFirst)
        self.addLast = button.Button("Add Last", 180, 330, self.addLast)
        self.removeLast = button.Button("Remove Last", 180, 390, self.removeLast)
        self.first = button.Button("First", 310, 330, self.first)
        self.last = button.Button("Last", 310, 390, self.last)
        self.size = button.Button("Size", 440, 330, self.size)
        self.isEmpty = button.Button("IsEmpty", 440, 390, self.isEmpty)
        
        # Doubly Linked List
        self.myStack = deque()
        self.counter=0
        
        self.window.configure(bg = "#ffffff")
        self.window.resizable(False, False)
        self.window.mainloop()

    def size(self):
        n=str(len(self.myStack))
        messagebox.showinfo("Size", n)

    def isEmpty(self):
        n=len(self.myStack)
        bool_value="False"
        if n > 0:
           bool_value="False"
           messagebox.showinfo("IsEmpty", bool_value)
        else:
           bool_value="True"
           messagebox.showinfo("IsEmpty", bool_value)

    def addFirst(self):
        if len(self.myStack) < 8:
            if len(self.myStack) == 0:
               number=len(self.myStack)
               self.counter = self.counter+1
               number2=str(self.counter)
               self.img.append(ImageTk.PhotoImage(Image.open(self.images[number])))
               self.labels.appendleft(self.canvas.create_text(530, 225, text="C"+number2, font=("Calibri")))
               self.text.appendleft("C")

               self.myStack.appendleft(self.canvas.create_image(500, 150, anchor=NW, image=self.img[number]))
                
            else: 
                for i in self.myStack:
                    self.canvas.move(i, -70, 0)

                for i in self.labels:
                    self.canvas.move(i, -70, 0)
   
                number=len(self.myStack)
                self.counter = self.counter+1
                number2=str(self.counter)
                self.img.append(ImageTk.PhotoImage(Image.open(self.images[number])))
                self.labels.appendleft(self.canvas.create_text(530, 225, text="C"+number2, font=("Calibri")))
                self.text.appendleft("C"+number2)

                self.myStack.appendleft(self.canvas.create_image(500, 150, anchor=NW, image=self.img[number]))

        else:
            messagebox.showerror("Error", "Queue is Full!")

    def addLast(self):
        if len(self.myStack) < 8:
            if len(self.myStack) == 0:
               number=len(self.myStack)
               self.img.append(ImageTk.PhotoImage(Image.open(self.images[number])))
               self.labels.append(self.canvas.create_text(530, 225, text="C1", font=("Calibri")))
               self.text.append("C1")
               
               self.myStack.append(self.canvas.create_image(500, 150, anchor=NW, image=self.img[number]))

            else: 
                number=len(self.myStack)
                self.counter = self.counter+1
                number2=str(self.counter)
                self.img.append(ImageTk.PhotoImage(Image.open(self.images[number])))
                self.labels.append(self.canvas.create_text(530-70*number, 225, text="C"+number2, font=("Calibri")))
                self.text.append("C"+number2)

                self.myStack.append(self.canvas.create_image(500-70*number, 150, anchor=NW, image=self.img[number]))

        else:
            messagebox.showerror("Error", "Queue is Full!")

    def removeFirst(self):
        if len(self.myStack) > 0:
            self.canvas.delete(self.myStack[0])
            self.canvas.delete(self.labels[0])
            self.labels.popleft()

            self.myStack.popleft()
            
            for i in self.myStack:
                    self.canvas.move(i, +70, 0)

            for i in self.labels:
                    self.canvas.move(i, +70, 0)

            self.text.popleft()

        else:
            messagebox.showerror("Error", "Queue is empty!")

    def removeLast(self):
        if len(self.myStack) > 0:
            self.canvas.delete(self.myStack[-1])
            self.myStack.pop()

            self.canvas.delete(self.labels[-1])
            self.labels.pop()
            self.text.pop()

        else:
            messagebox.showerror("Error", "Queue is empty!")

    def first(self):
        if len(self.myStack) != 0:
            messagebox.showinfo("First", self.text[0])
        else:
            messagebox.showerror("Error", "Queue is empty!")

    def last(self):
        if len(self.myStack) != 0:
            messagebox.showinfo("Last", self.text[-1])
        else:
            messagebox.showerror("Error", "Queue is empty!")

p1 = Main()