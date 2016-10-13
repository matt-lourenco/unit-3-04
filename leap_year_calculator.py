# Created by: Matthew Lourenco
# Created on 13 Oct 2016
# This program calculates whether a year is a leap year or not

import ui

def calculate_touch_up_inside(sender):
    #Check if entered year is an integer
    
    year = view['year_textfield'].text
    try:
        year = int(year)
    except:
        view['reply_label'].text = '"' + str(year) + '"' + ' is not an integer.'
    #Check for leap year
    if (int(year) % 4) == 0:
        if (int(year) % 100) == 0:
            if (int(year) % 400) == 0:
                view['reply_label'].text = 'The year ' + str(year) + ' is a leap year.'
            else:
                view['reply_label'].text = 'The year ' + str(year) + ' is not a leap year.'
        else:
            view['reply_label'].text = 'The year ' + str(year) + ' is a leap year.'
    else:
        view['reply_label'].text = 'The year ' + str(year) + ' is not a leap year.'

view = ui.load_view()
view.present('full_screen')
