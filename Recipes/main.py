# This is the file to run  when starting the website
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) # set debug to false when running in production

