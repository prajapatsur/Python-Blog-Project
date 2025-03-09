from website import create_app

if __name__=="__main__":
    app=create_app()
    app.run(debug=True)     #for another port --> app.run(debug=True, port=1000) --> http://127.0.0.1:1000/