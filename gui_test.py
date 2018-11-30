from guizero import App, Text, TextBox, PushButton

def display_mode():
    message1.value = name.value


app = App(title = 'Control Pannel')

message1 = Text(app, text = 'PARKING', size = 20, color = 'red')

message2 = Text(app, text = 'DRIVING', size = 20, color = 'red')

name = TextBox(app, width = 40)

update_text = PushButton(app, command = display_mode, text = 'Display mode')

app.display()