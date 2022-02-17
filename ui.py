from cgitb import text
import time
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class GUI:
    def __init__(self,quiz_brain: QuizBrain):
        
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("QUIZZLER")
        self.window.config(bg=THEME_COLOR,padx=30,pady=30)
        self.canvas=Canvas(height=250,width=600)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.canvas.config(bg="white",highlightthickness=0)
        self.question_text=self.canvas.create_text(300,125,text= "question",width= 580,font=("Arial",20,"italic"),fill=THEME_COLOR)
        right_image= PhotoImage(file="images/true.png")
        wrong_image= PhotoImage(file="images/false.png")
        self.true_button= Button(image= right_image,command= self.right_press)
        self.true_button.grid(row=2,column=0)
        self.false_button= Button(image= wrong_image,command=self.wrong_press)
        self.false_button.grid(row=2,column=1)
        self.score_label=Label(text= f"Score: {self.quiz.score}",font=("Arial", 18,"bold"),fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        self.display_question()
        
        self.window.mainloop()
    
    def display_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text= f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have finished The quiz.\nFinal Score:{self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def right_press(self):
        self.feed_back(self.quiz.check_answer("false"))

    def wrong_press(self):
        self.feed_back(self.quiz.check_answer("false"))
        
    
    def feed_back(self, is_right):
        if(is_right):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.display_question)
        