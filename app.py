import gradio as gr

def calculate_bmi(name, height_in_cm, weight):
    try:
        if height_in_cm <= 0:
            raise ValueError("Die Höhe muss einen positiven Wert haben.")
        if weight <= 0:
            raise ValueError("Das Gewicht muss einen positiven Wert haben.")
        
        BMI = weight / (height_in_cm / 100) ** 2
    except ZeroDivisionError:
        return "Fehler: Die Höhe darf nicht null sein.", ""
    except TypeError:
        return "Fehler: Ungültiger Wert für Höhe oder Gewicht.", ""
    except ValueError as e:
        return "Error: " + str(e), ""
    
    output1 = 'Hallo %s, dein BMI beträgt %.2f' % (name, BMI)
    if BMI <= 18.4:
        output2 = "Du bist untergewichtig."
    elif BMI <= 24.9:
        output2 = "Du bist gesund."
    elif BMI <= 29.9:
        output2 = "Du bist übergewichtig."
    else:
        output2 = "Du bist stark übergewichtig."
    return output1, output2

bmi_cal = gr.Interface(fn=calculate_bmi, inputs=['text', 'number', gr.components.Slider(0, 120)], outputs=['text', 'text'])
bmi_cal.launch()

