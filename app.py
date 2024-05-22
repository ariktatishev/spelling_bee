from flask import Flask, request, render_template
from spelling_bee import get_words

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        letters_input = request.form.get("letters")
        if not letters_input or len(letters_input) != 7:
            return '''
            Please enter all 7 letters with the center letter uppercase.<br>
            <a href="/"><button>Go Back</button></a>
            ''', 400

        # Extract the center (uppercase) letter and the other letters
        center_letter = None
        letters = []
        for letter in letters_input:
            if letter.isupper():
                center_letter = letter.lower(
                )  # Convert to lowercase for consistency
            else:
                letters.append(letter)

        # Ensure that a center letter was provided and is uppercase
        if center_letter is None:
            return '''
            Please make sure the center letter is uppercase.<br>
            <a href="/"><button>Go Back</button></a>
            ''', 400

        # You might want to add the center letter to the list of letters,
        # depending on your get_words function's needs
        letters.append(center_letter)
        possible_words = get_words(letters, center_letter)
        return render_template("result.html", words=possible_words)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
