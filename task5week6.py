import gradio as gr

def square_number(x):
    return x ** 2

# Create interface
demo = gr.Interface(fn=square_number, inputs="number", outputs="number", title="Square Calculator")

# Launch the app
demo.launch( share=True)
