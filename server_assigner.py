import sys
import csv
import os

def die_n_print_help():
    print('Usage: python server_assigner.py list_file.csv')
    print('-'*25)
    print('Creates a directory called "server_assignments" and generates handouts')
    sys.exit(1)

if len(sys.argv) != 2:
    print('-'*25)
    print('Not enough arguments! Or too many?')
    print('-'*25)
    die_n_print_help()

people = []
try:
    with open(sys.argv[1], 'r') as list_file:
        print('Reading list file...')
        reader = csv.reader(list_file, delimiter=',')
        for row in reader:
            people.append(row)
except:
    print('-'*25)
    print('Problem reading list file. Is it not a CSV?')
    die_n_print_help()

# The first row is a header.
people = people[1:]

try:
    with open('./template_linux.html', 'r') as html_file:
        print('Reading linux template...')
        linux_html = html_file.read()
except:
    print('-'*25)
    print('Somethings wrong with your linux template HTML file.')
    print('The script is looking for a file called "template_linux.html"')
    die_n_print_help()

try:
    with open('./template_windows.html', 'r') as html_file:
        print('Reading windows template...')
        windows_html = html_file.read()
except:
    print('-'*25)
    print('Somethings wrong with your windows template HTML file.')
    print('The script is looking for a file called "template_windows.html"')
    die_n_print_help()

def replacer(text, replacements):
    for i, j in replacements.items():
        text = text.replace(i, j)
    return text


print('Replacing values...')
print('-'*25)
for i in range(len(people)):

    replacements = {
        'HOST-EIP' : people[i][0],
        'HOST-IIP' : people[i][1],
        'HOST-TYPE' : people[i][2],
        'USER-NAME' : people[i][3],
        'OS-NAME' : people[i][4],
        'OS-PASSW' : people[i][5],
        'SPLK-NAME' : people[i][6],
        'SPLK-PASSW' : people[i][7],
        'USER-ID' : people[i][1][-2:]
    }

    if 'linux_student' in replacements['HOST-TYPE']:
        new_html = replacer(linux_html, replacements)
    elif 'windows_student' in replacements['HOST-TYPE']:
        new_html = replacer(windows_html, replacements)
    else:
        print('Skipping {}...'.format(replacements['HOST-TYPE']))
        continue

    # No added number at the end there
    if people[i][3] != 'demo':
        name = people[i][3][:-2]
    else:
        name = 'demo'

    try:
        if not os.path.exists('server_assignments'):
            os.makedirs('server_assignments')
    except:
        print('-'*25)
        print('Cant make new directory here. Permissions maybe?')
        die_n_print_help()

    try:
        with open('./server_assignments/{}.html'.format(name), 'w') as f:
            f.write(new_html)
        print('./server_assignments/{}.html'.format(name))
    except:
        print('-'*25)
        print('Cant write the new html file.')



print('-'*25)
print('Done!')
