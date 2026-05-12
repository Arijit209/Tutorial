from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

# from app import create_app, db

# app = create_app()

# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
#         print("Tables created successfully 🚀")

#     app.run(debug=True)