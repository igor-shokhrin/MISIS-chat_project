from flask import Flask, render_template, request, url_for, jsonify
import kontakt, vk
app = Flask(__name__)

@app.route('/tests/endpoint', methods=['POST'])
def my_test_endpoint():
    input_json = request.get_json(force=True)
    # force=True, above, is necessary if another developer
    # forgot to set the MIME type to 'application/json'
    print ('data from client:', input_json)
    print(input_json['cmd'])
    if(input_json['cmd'] == 'VK_Autorization'):
        try:
            kontakt.get_user_photo(input_json['username'],input_json['password'])
        except vk.exceptions.VkAuthError:
            return jsonify({'answer' : 'Incorrect username or password'})
    return jsonify({'answer':'Autorization OK'})

if __name__ == '__main__':
    app.run(debug=True)
    print("sad")


