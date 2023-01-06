import PySimpleGUI as sg


def theme(vis):
    sg.theme(vis)
    menu_top = sg.Menu
    layout = [
            [
                sg.Input(key='-INPUT-'),
                sg.Combo(values=['Km to Mile', 'Kg to Pound', 'Seconds to Mins'], default_value='Select One',
                         readonly=True, text_color=None, size=20, key='-UNITS-'),
                sg.Button('Convert', bind_return_key=True, key='-CONVERT-')
            ],
            [sg.Text('Output', key='-OUTPUT-')],
            [sg.Button('Close', k='-CLOSEE-')]
    ]

    layout_1 = [
            [
                sg.Input(k='-IMPERIAL-'),
                sg.Combo(values=['Mile to Km', 'Pound to Kg', 'Mins to Seconds'], default_value='Select One',
                         readonly=True, text_color=None, size=20, k='-METRIC-'),
                sg.Button('Convert', bind_return_key=True, k='-CONVERSION1-')
            ],
            [sg.Text('Output', k='-OUTPUT1-')],
            [sg.Button('Close', k='-CLOSE-')]
    ]

    group = [[menu_top([['File', ['Exit']], ['Edit', ['Reset']]])],
             [sg.TabGroup([[sg.Tab('Metric to Imperial', layout),
              sg.Tab('Imperial to Metric', layout_1)]])]
             ]

    window = sg.Window('Converter', group, size=(600, 200), auto_size_text=True, resizable=True)
    return window


def main():

    window = theme(sg.theme())

    while True:
        event, values = window.read()
        print(event, values)

        if event in (sg.WIN_CLOSED, '-CLOSE-', '-CLOSEE-', 'Exit'):
            break

        if event == '-CONVERT-':
            output_string = ''
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
            else:
                window['-OUTPUT-'].update('Please Enter a Number')
            window['-OUTPUT-'].update(output_string)

        if event == '-CONVERSION1-':
            output_strin = ''
            input1_value = values['-IMPERIAL-']
            if input1_value.isnumeric():
                match values['-METRIC-']:
                    case 'Mile to Km':
                        output1 = round(float(input1_value) / 0.6214, 2)
                        output_strin = f'{input1_value} Miles are {output1} Km.'
                    case 'Pound to Kg':
                        output1 = round(float(input1_value) / 2.20462, 2)
                        output_strin = f'{input1_value} Pound(s) are {output1} Kg(s).'
                    case 'Mins to Seconds':
                        output1 = round(float(input1_value) * 60, 2)
                        output_strin = f'{input1_value} Min(s) are {output1} Second(s).'
            else:
                window['-OUTPUT1-'].update(output_strin)
            window['-OUTPUT1-'].update(output_strin)


    window.close()


main()
