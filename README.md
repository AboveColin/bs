# BS

BS is a data extraction tool designed to streamline the process of retrieving information. It offers a range of functionalities, from querying specific data to saving and sharing the results. The tool is compatible with Google Chrome and can be easily set up and executed on a machine with Python 3.6 installed.

## Prerequisites

- Google Chrome Browser
- ChromeDriver binary compatible with your Chrome version
- Python 3.6 or higher

## Installation

Clone the repository and install the required dependencies using the following commands:

```sh
git clone <repository-link>
cd <repository-directory>
pip install -r requirements.txt
```

## Usage

Execute the `main.py` script with appropriate arguments to start the search process:

```sh
python main.py <arguments>
```

### Arguments

#### Mode (One of the following is **REQUIRED**)

- **Composer Mode:**
  - Search by composer name.
  - Use: `-c "composer name"` or `--composer "composer name"`
  
- **Title Mode:**
  - Search by title name.
  - Use: `-t "title name"` or `--title "title name"`
  
- **Author Mode:**
  - Search by author name.
  - Use: `-a "author name"` or `--author "author name"`

#### Optional

- **List Mode:**
  - Display all information in a list without interruptions.
  - Use: `-l` or `--list`
  
- **Proxy:**
  - Access data using a specific proxy.
  - Use: `-p "127.0.0.1:1234"` or `--proxy "127.0.0.1:1234"`
  
- **Without Headless:**
  - Launch the script with the browser window visible.
  - Use: `-whl` or `--without_headless`
  
- **Save:**
  - Save the output to a text file located in the `saves/` directory.
  - Use: `-s` or `--save`
  
- **SQL:**
  - Store the data in a MySQL database.
  - Use: `-sql` or `--sql`
  
- **Discord Webhook (requires SQL to be enabled):**
  - Send new database entries to a specified Discord webhook.
  - Use: `-dwh` or `--discord_webhook`

## Examples

Search for information by composer name, display it in list form, and save the output to a text file:

```sh
python main.py -c "Beethoven" -l -s
```

Retrieve data by title, use a proxy for the connection, and save the results to a MySQL database:

```sh
python main.py -t "Moonlight Sonata" -p "127.0.0.1:1234" -sql
```

## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgements

- Thanks to everyone who contributed to the development and enhancement of this tool.

---
