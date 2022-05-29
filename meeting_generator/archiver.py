import os
import shutil
import glob
import random
import markdown

path_source = r'C:\Users\cferguson\OneDrive - fairlife, LLC\BI\Code\Programming\data_colloquium'
sourcefiles = os.listdir(path_source)

path_destination_archive = r'C:\Users\cferguson\OneDrive - fairlife, LLC\BI\Code\Programming\data_colloquium\archive'

exclude_files = ['template.md', 'README.md']

path_template       = r'\template.md'
path_template_new   = r'\yyyy-mm-dd.md'

def archiver():

    """

     move all markdown (except template.md & readme.md) files into archive directory

    """

    try:

        for file in sourcefiles:

            if file.endswith('.md') and file not in exclude_files:
                shutil.move(os.path.join(path_source, file), os.path.join(path_destination_archive, file))

        print('file archived successfuly')

    except:

        print('file archiving error')

archiver()

list_of_users = [
                     ":octopus: user1"
                    ,":duck: user2"
                    ,":beer: user3"
                    # ,":cactus: user5"
                    ,":dog: user4"
                    # ,":hatching_chick: user6"
                ]

random.shuffle(list_of_users)


list_of_users_formatting = []

for user in list_of_users:
    list_of_users_formatting.append(
f'''{user}
- current projects:
    - insert text here
- other updates:
    - insert text here

--

'''
)

template_top = '''
```
 _____  ___ _____ ___    _____ _____ _      _     _____  _____ _   _ _____ _   _ __  __
|  _  \/ _ \_   _/ _ \  /  __ \  _  | |    | |   |  _  ||  _  | | | |_   _| | | |  \/  |
| | | / /_\ \| |/ /_\ \ | /  \/ | | | |    | |   | | | || | | | | | | | | | | | | .  . |
| | | |  _  || ||  _  | | |   | | | | |    | |   | | | || | | | | | | | | | | | | |\/| |
| |/ /| | | || || | | | | \__/\ \_/ / |____| |___\ \_/ /\ \/' / |_| |_| |_| |_| | |  | |
|___/ \_| |_/\_/\_| |_/  \____/\___/\_____/\_____/\___/  \_/\_\\___/ \___/ \___/\_|  |_/

```

### **:date: YYYY-MM-DD**

#

#### **:clipboard: agenda**
- user updates
    - projects/tasks/initiatives currently working on
    - ancillary items
- tech news/general updates
- chart review

#

#### **:raising_hand: user updates**

--

'''

template_bottom = '''#

#### **:newspaper: general news/updates**
-

#

#### **:bar_chart: chart review**
-

#

##### :wave: :new_moon: [so long, farewell, auf wiedersehen, good night](https://www.youtube.com/watch?v=dQw4w9WgXcQ) :new_moon: :wave:

#
'''

with open(r'C:\Users\cferguson\OneDrive - fairlife, LLC\BI\Code\Programming\data_colloquium\yyyy-MM-dd.md', 'w') as f:
    f.write(template_top)
    f.writelines(list_of_users_formatting)
    f.write(template_bottom)


# ------------- #
# bibliography

# this website taught me how to exclude files
# https://stackoverflow.com/questions/36945916/python-move-files-from-one-folder-to-other-with-some-exceptions

# this website taught me how to rename files
# https://pythonguides.com/python-copy-file/