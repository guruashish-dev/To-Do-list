from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

# Route to render the To-Do List page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle adding a task
@app.route('/add-task', methods=['POST'])
def add_task():
    task_name = request.form.get('task')
    if task_name:
        # Optionally, pass this task to a Java program for processing
        java_output = subprocess.run(
            ['java', 'TodoListHandler', task_name], 
            capture_output=True, text=True
        )
        return jsonify({'status': 'success', 'task': task_name, 'java_output': java_output.stdout})
    return jsonify({'status': 'error', 'message': 'Task is empty!'})

if __name__ == '__main__':
    app.run(debug=True)
