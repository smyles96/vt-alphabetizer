![Python 3 Badge](https://img.shields.io/badge/Python-3.x-green)

# Alphabetizer

### Requirements to Run the Code
* Python 3.x is installed on your system
* The `python3` executable directory is in your system path

### Obtaining and Running the Code
1. Clone this repository

    ```bash
    git clone https://github.com/smyles96/vt-alphabetizer.git
    ```

2. Change into its directory

    ```bash
    cd vt-alphabetizer
    ```

3. Run the main alphabetizer.py script to start an interactive terminal prompt

    ```bash
    # On Linux
    chmod +x ./alphabetizer.py
    ./alphabetizer.py

    # On Windows
    python3 alphabetizer.py
    ```

4. The program will continually ask for a string to alphabetize. After inputting one the program will output the letters in alphabetized order.

    ```bash
    ./alphabetize.py

    Enter a string to alphabetize (or CTRL-C to stop): Virginia Tech
    aceghiiinrTV
    Enter a string to alphabetize (or CTRL-C to stop): 3 Blind Mice
    BcdeiilMn
    Enter a string to alphabetize (or CTRL-C to stop): Turtle
    elrTtu
    Enter a string to alphabetize (or CTRL-C to stop): <CTRL-C>
    Exiting...
    ```

5. To quit, press `CTRL+C`
6. For help, run the script with extra arguments (ex. `./alphabetize.py help`)