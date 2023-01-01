import PySimpleGUI as sg

layout = [
    [
        sg.Input(key='-INPUT-'),
        sg.Spin(['Km to Mile', 'Kg to Pound', 'Seconds to Mins'], size=20, key='-UNITS-'),
        sg.Button('Convert', key='-CONVERT-')
    ],
    [sg.Text('Output', key='-OUTPUT-')],
    [sg.Button('Close')]
]

window = sg.Window('Converter', layout, use_custom_titlebar=True, size=(600, 200), resizable=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Close':
        break

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'Km to Mile':
                    output = round(float(input_value) * 0.6214, 2)
                    output_string = f'{input_value} Km are {output} Miles.'
                case 'Kg to Pound':
                    output = round(float(input_value) * 2.20462, 2)
                    output_string = f'{input_value} Kg are {output} Pounds.'
                case 'Seconds to Mins':
                    output = round(float(input_value) / 60, 2)
                    output_string = f'{input_value} Seconds are {output} Mins.'

            window['-OUTPUT-'].update(output_string)
        else:
            window['-OUTPUT-'].update('Please Enter a Number')

window.close()

