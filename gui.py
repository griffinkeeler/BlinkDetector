import FreeSimpleGUI as sg
from time import sleep

from FreeSimpleGUI import SYMBOL_CIRCLE

# Outputs  "3...2...1" one
# character at a time.
def countdown(window):
    for i in range(0, 3):
        if i == 0:
            # Allows communication between thread and main thread.
            window.write_event_value(('-THREAD-', '-TITLE-'), i)
            window.write_event_value(('-THREAD-', '-THREE-'), i)
        if i == 1:
            window.write_event_value(('-THREAD-', '-TWO-'), i)
        if i == 2:
            window.write_event_value(('-THREAD-', '-ONE-'), i)
        for c in range(0, 3):
            sleep(0.33)
            if i == 0:
                if c == 0:
                    window.write_event_value(('-THREAD-', '-PERIOD1-'), c)
                if c == 1:
                    window.write_event_value(('-THREAD-', '-PERIOD2-'), c)
                if c == 2:
                    window.write_event_value(('-THREAD-', '-PERIOD3-'), c)
                    sleep(0.33)
            if i == 1:
                if c == 0:
                    window.write_event_value(('-THREAD-', '-PERIOD4-'), c)
                if c == 1:
                    window.write_event_value(('-THREAD-', '-PERIOD5-'), c)
                if c == 2:
                    window.write_event_value(('-THREAD-', '-PERIOD6-'), c)
                    sleep(0.33)


# The primary layout for the GUI.
def window_one():
    return   [[sg.Push(), sg.Text("Blink Calibrator", text_color='white', auto_size_text=True), sg.Push()],
              [sg.Push(), sg.Text('Press "Begin" to start calibration.', text_color='gold'), sg.Push()],
              [sg.Push(), sg.Text(key='-INTRO-'), sg.Push()],
              [(sg.Text(key='-DIGIT_ONE-', text_color='white'),
                    sg.Text(key='-P1-', text_color='white'),
                    sg.Text(key='-P2-', text_color='white'),
                    sg.Text(key='-P3-', text_color='white'),
                    sg.Text(key='-DIGIT_TWO-', text_color='white'),
                    sg.Text(key='-P4-', text_color='white'),
                    sg.Text(key='-P5-', text_color='white'),
                    sg.Text(key='-P6-', text_color='white'),
                    sg.Text(key='-DIGIT_THREE-', text_color='white'))],
              [sg.Push(), sg.Button('Begin'), sg.Push()],
              [sg.Text(key='-MESSAGE-')]
              ]

# Creates a second window
# TODO: Not sure how to implement this yet. 
def window_two():
    layout =  [[sg.Text('Window Two')],
               [sg.Button('button')]
               ]
    new_window = sg.Window("Window Two", layout)
    while True:
        events, value = new_window.read()


# Window is created.
window = sg.Window("Blink Calibrator", window_one())

# Event loop.
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    window['-MESSAGE-'].update(f'{event}')
    if event == 'Begin':
        # Begins the thread
        window.start_thread(lambda: countdown(window), ('-THREAD-', '-THREAD ENDED-'))
    # A series of if statements that update the corresponding
    # window to based on the event received from the main
    # thread.
    elif event[0] == '-THREAD-':
        if event [1] == '-THREE-':
            window['-DIGIT_ONE-'].update('3')
            window['-INTRO-'].update('Beginning in: ')
        elif event [1] == '-TWO-':
            window['-DIGIT_TWO-'].update('2')
        elif event [1] == '-ONE-':
            window['-DIGIT_THREE-'].update('1')
        elif event [1] == '-PERIOD1-':
            window['-P1-'].update('.')
        elif event [1] == '-PERIOD2-':
            window['-P2-'].update('.')
        elif event [1] == '-PERIOD3-':
            window['-P3-'].update('.')
        elif event [1] == '-PERIOD4-':
            window['-P4-'].update('.')
        elif event [1] == '-PERIOD5-':
            window['-P5-'].update('.')
        elif event [1] == '-PERIOD6-':
            window['-P6-'].update('.')













