from flask import request, jsonify,Flask

app = Flask(__name__)
notes = [
    {'id':1,'title':'My First Note','content':'hello'},
    {'id':2,'title':'My 2 Note','content':'goodbye'}
]
@app.route('/notes',methods=['GET'])

def get_all_notes():
    return jsonify({'notes':notes})
@app.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    note = None
    for i in notes:
        if i['id'] == note_id:
            note = i
            break
    if note == None:
        return jsonify({'Not found!'}),404
    return jsonify({'note':note})
@app.route('/add_notes', methods=['POST'])
def create_note():
    data = request.json()

    if not data or 'title' not in data or 'content' not in data:
        return jsonify({'Title is empty!'}),400
    new_note = {
        'id':len(notes) + 1,
        'title':data['title'],
        'note':data['content']}
    

    notes.append(new_note)

    return jsonify({'message':'New note created!','note':new_note}),201
if __name__ == '__main__':
    app.run()
