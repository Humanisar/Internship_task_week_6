import gradio as gr

def reverse_sentence(sentence):
    return sentence[::-1]

# Create interface
demo = gr.Interface(fn=reverse_sentence, inputs="text", outputs="text", title="Sentence Reverser")

# Launch the app
demo.launch( share=True)
