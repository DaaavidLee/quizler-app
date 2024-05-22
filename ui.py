THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # canvas
        self.canvas = Canvas()
        self.canvas.config(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150, 125, width=280,
            text="Some text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )

        # labels
        self.label = Label(text="Score: ", fg="white", bg=THEME_COLOR)
        self.label.grid(row=0, column=1)

        # images
        cross_img = PhotoImage(file="images/false.png")
        click_img = PhotoImage(file="images/true.png")


        # buttons
        self.cross_button = Button(image=cross_img, highlightthickness=0, command=self.true_pressed)
        self.cross_button.grid(row=2, column=0)

        self.click_button = Button(image=click_img, highlightthickness=0, command=self.false_pressed)
        self.click_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.cross_button.config(state="disable")
            self.click_button.config(state="disable")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
