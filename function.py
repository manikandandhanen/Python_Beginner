def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2  # center of text
    print(" " * left_margin, text)


def centre_text(text):
    text = str(text)  # str function to convert the argument that was passed to a string
    left_margin = (80 - len(text)) // 2  # center of text
    print(" " * left_margin, text)


# call the function
centre_text("spam and egs")
centre_text("spam, spam and eggs")
centre_text(12)  # integer get converted to string
centre_text("spam, spam, spam and spam")
python_food()
