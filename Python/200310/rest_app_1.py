from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello~</h1>'

@app.route('/rest/v1/data', methods=['GET'])
def data_get():
    
    data_dic = [
        {
        'id' : 'cool',
        'name' : 'jane',
        'pw' : 'password1'
        },
        {
        'id' : 'cool',
        'name' : 'jane',
        'pw' : 'password1'
        }
    ]

    return jsonify({'members':data_dic})

# path variable
@app.route('/rest/v1/leds/<int:led_id>', methods=['GET'])
def led_get(led_id):
    
    data_dic = {'led_no': led_id}

    if led_id > 9:
        abort(404)

    return jsonify(data_dic)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error' : 'Not Used Led Number'}))


if __name__ == '__main__' :
    app.run(debug=True)