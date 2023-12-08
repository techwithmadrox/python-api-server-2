from app import app

print("DEBUG __NAME___ IS: " + __name__)
print("DEBUG __MAIN___ IS: " + '__main__')

if __name__ == '__main__':
    app.run(debug=True)