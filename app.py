import gradio as gr
from gradio_calendar import Calendar
import datetime

def is_weekday(date: datetime.datetime):
    weekday = str(date.weekday()) 
    return date.weekday() 

with gr.Blocks() as demo:
    gr.Markdown(
    """
    # VICTOR's 心情章魚
    Start typing below to see the output.
    心情指數 0(差)~10(好)
    """)
    with gr.Row():
        num1 = gr.Slider(1, 10)
    output = gr.Image("1.png")



    @gr.on(inputs=[num1], outputs=output)
    def sum(num1):
        if num1>=1 and num1<=5:
            b="2.png"
        else :
            b="1.png"
        return b

 


demo.launch(share=True) 