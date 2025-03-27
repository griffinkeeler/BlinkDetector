import FreeSimpleGUI as sg
from time import sleep

# The primary layout for the GUI.
layout = [[sg.Push(), sg.Text("Blink Calibrator"), sg.Push()],
          [sg.Graph((400, 400), (0, 0),
                    (400, 400), key='-GRAPH-', background_color='white')],
          [sg.Push(), sg.Button('Begin'), sg.Push()]
          ]

# Window
window = sg.Window("Blink Calibrator", layout)

# Allows the graph to be modified before a window.read() call
window.finalize()

# Adds text middle of the graph.
window['-GRAPH-'].draw_text('Press "Begin" \n to start calibration.', (200, 200))

# Loops through the window until it is closed.
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

