To run the app:

1) Put the (unzipped) folder "movie_app" in your working directory (in VS Code: next to the ".venv" folder in the Explorer window), with all its files inside
2.1) Open the terminal (Terminal > New Terminal) and make sure your command line starts with (a usually green-colored) "(.venv)", to confirm you are connected to your virtual environment
2.2) Open "movie_app.py" and "recommender.py", and see if you are missing any of the imported libraries (if so, they will likely be underlined in yellow)
2.3) Install the missing libraries (if any) by running "python pip install <name of the library>" in the terminal, for all missing libraries
3) In the terminal, launch the app by running "streamlit run movie_app\movie_app.py", which should either automatically open a browser window, or print a URL adress to be copied and pasted in a browser window