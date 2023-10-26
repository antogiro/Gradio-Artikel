import gradio as gr
import pandas as pd

# Read the CSV file into a DataFrame
g_dist_in_ed = pd.read_csv('gender_distribuation_in_education.csv').groupby(['Gender', 'Education']).size().reset_index(name="Count")

# Read another CSV file into a DataFrame
student_test_data = pd.read_csv('student_test_data.csv')

# Define a function to create a bar plot based on user input
def bar_plot_fn(display):
    if display == "simple":
        return gr.BarPlot(
            student_test_data,
            x="Name",
            y="total score",
            title="Student Test Data",
            tooltip=["Name", "total score"],
            width=500,
            interactive=True,
            show_actions_button=True,
        )
    elif display == "stacked":
        return gr.BarPlot(
            g_dist_in_ed,
            x="Gender",
            y="Count",
            color="Education",
            title="Gender Distribuation in Education",
            tooltip=["Count", "Education"],
            width=200,
            height=400,
            show_actions_button=True,
        )
    
# Create a Gradio Blocks interface
with gr.Blocks() as bar_plot:
    with gr.Row():
        with gr.Column():
            # Dropdown for selecting the type of bar plot
            display = gr.Dropdown(
                choices=[
                    "simple",
                    "stacked"
                ],
                value="simple",
                label="Type of Bar Plot",
            )
        with gr.Column():
            # Bar plot widget
            plot = gr.BarPlot()
    # Set the change function for the dropdown input and link it to the bar plot output
    display.change(bar_plot_fn, inputs=display, outputs=plot)
    bar_plot.load(fn=bar_plot_fn, inputs=display, outputs=plot)

# Launch the Gradio interface
bar_plot.launch()