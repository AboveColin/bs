# BS
 
## Requirements:
- Google Chrome 
- ChromeDriver binary
- Python 3.6
## How To Install
```
pip install -r requirements.txt
```
###
To start, use
``python main.py``

## Arguments

- Mode (**REQUIRED**)
  - `--composer "name"`, `-c "name"`
  
  or
  - `--title "name"`, `-t "name"`
  
  or
  - `--author "name"`, `-a "name"`
> Use one of the above 3, to search in the appropiate mode

- `--list`, `-l` 
> Displays all info in a list form, without interruptions

- `--proxy "127.0.0.1:1234"`, `-p "127.0.0.1:1234"`
> Use a proxy when accessing data

- `--without_headless`, `-whl`
> Launch the python script without headless mode on.

- `--save`, `-s`
> Saves the output to a .txt file in the ``saves/`` folder

- `--sql`, `-sql`
> Saves all the data to a MySQL server.

- `--discord_webhook`, `-dwh` (*Requires --SQL to work properly*)
> Send new entries to a discord webhook


