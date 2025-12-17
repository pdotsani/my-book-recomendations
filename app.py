from flask import Flask, jsonify
from storygraph_api import User, Book
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


@app.route('/get-recomendation', methods=['GET'])
def get_recomendation():
    cookie = os.getenv("COOKIE")
    uname= os.getenv("UNAME")

    user = User();
    to_read = user.to_read(uname, cookie)

    books_to_read = to_read.length
    random_book = random.choice(books_to_read)

    book = Book();
    book_info = book.book_info(random_book.book_id)
    
    book_image_url = book_info.book_cover
    
    return jsonify({
        "url": book_image_url
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

