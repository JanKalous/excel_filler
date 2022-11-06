import PySimpleGUI as sg
import pandas as pd

sg.theme("DarkTeal9")

#file import to pandas
EXCEL_FILE = r"some excel file"
df = pd.read_excel(EXCEL_FILE)

#form layout 
form_layout = [
    [sg.Text("Kniha jízd pro ---")],
    [sg.Text("Datum                             ", size=(15,1)), sg.InputText(key="Datum")],
    [sg.Text("Trasa                             ", size=(15,1)), sg.InputText(key="Trasa cesty")],
    [sg.Text("Účel                              ", size=(15,1)), sg.InputText(key="Účel")],
    [sg.Text("Stav tachometru                   ", size=(15,1)), sg.InputText(key="Stav tachometru")],
    [sg.Text("Ujeté km                          ", size=(15,1)), sg.InputText(key="Ujeté km")],
    [sg.Text("Bezp. přestávka      "), sg.Combo(["Ano", "Ne"], key="Bezp. Přestávka")],
    [sg.Text("Doplnění PHM         "), sg.Combo(["Ano", "Ne"], key="Doplnění PHM")],
    [sg.Text("Jméno řidiče                        ", size=(15,1)), sg.InputText(key="Jméno řidiče")],
    [sg.Submit(),sg.Button("Clear"),sg.Exit()]
]

#window inicialization
window = sg.Window("Kniha Jízd", form_layout)

#Clear button function
def clear_input():
    for key in values:
        window[key]("")
    return None

#Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Clear":
        clear_input()
    if event == "Submit":
        df = df.append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup("Data uloženy :)")
        clear_input()

window.close()
