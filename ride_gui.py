# ride_gui.py
'''
Create a GUI with PySimpleGUI to write information about a single ride to csv.
'''
import csv
import daily_report
import PySimpleGUI as sg


def show_gui():
    '''
    Display GUI to enter ride info.
    '''
    sg.theme('DarkGreen5')

    layout = [
        [sg.Text('Date'), sg.Input(key='Date'),
         sg.CalendarButton('...', format='%Y-%m-%d')],
        [sg.Text('Kilometers'), sg.Input(key='km')],
        [sg.Radio('Outside', 'Radio1', key='Outside'),
         sg.Radio('Zwift', 'Radio1', default=True, key='Zwift')],
        [sg.Button('Submit', bind_return_key=True), sg.Button('Cancel')]
    ]

    window = sg.Window('Enter Ride Data', layout, font=('Arial 10'))

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        elif event == 'Submit':
            date = values['Date']
            km = values['km']
            location = ''
            if values['Outside']:
                location = 'outside'
            else:
                location = 'zwift'

            with open('rides.csv', 'a', newline='') as csvfile:
                ride_writer = csv.writer(csvfile, delimiter=',')
                ride_writer.writerow([date, km, location])
            break
    window.close()


def main():
    show_gui()
    daily_report.make_report()


if __name__ == '__main__':
    main()
