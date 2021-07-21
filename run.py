from market import app

#Checks if the run.py file has executed directly and not been imported
if __name__ == '__main__':
    app.run(debug=True)