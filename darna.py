##Sets up the flask server for viewing the folder locally at {ip_address}:3001
from flask import Flask, render_template, send_from_directory, session, request, redirect
import os, subprocess
import getpass
import variables



app = Flask(__name__)
app.secret_key = 'your_secret_key_jjkjdhbclskdbvlkdfv'

folderpath = variables.HS_path
ip_address = variables.ip_address
user = variables.user
pwd = variables.pwd
nextcloud_url = f"https://{ip_address}:8080/remote.php/dav/files/{user}/Darnahi"
# Configure static folder path
app.static_folder = 'static'

"""@app.route('/')
def index():
    return render_template('index.html', ip_address=ip_address)"""

@app.route('/')
def home():
    if 'logged_in' in session:
        # User is logged in, redirect to the protected page
        return render_template('index.html')
    else:
        # User is not logged in, redirect to the login page
        return redirect('/login')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']

        # Check if the password is correct
        if password == 'health':
            # Password is correct, set the login status in the session
            session['logged_in'] = True
            return redirect('/')
        else:
            # Password is incorrect, show an error message
            error_message = 'Invalid password. Please try again.'
            return render_template('login.html', error_message=error_message)

    # Render the login page template
    return render_template('login.html')


@app.route('/logout')
def logout():
    # Remove the login status from the session
    session.pop('logged_in', None)
    return redirect('/login')


@app.route('/folder')
@app.route('/folder/<path:foldername>')
def folder_index(foldername=None):
    if 'logged_in' not in session:
        return redirect('/login')
    
    folder_path = folderpath
    if foldername:
        folder_path = os.path.join(folder_path, foldername)
    command = f"ls -l {folder_path}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    files = result.stdout.splitlines()
    file_links = []

    for file in files:
        file_info = file.split()
        filename = file_info[-1]
        is_directory = file_info[0].startswith("d")

        if is_directory:
            if foldername:
                file_links.append({'filename': filename, 'path': f'/folder/{foldername}/{filename}/', 'is_folder': True})
            else:
                file_links.append({'filename': filename, 'path': f'/folder/{filename}/', 'is_folder': True})
        else:
            file_links.append({'filename': filename, 'path': f'/{filename}', 'is_folder': False})

    return render_template('folder_index.html', files=file_links)

@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory(folderpath, filename, as_attachment=False)

@app.route('/folder/<path:foldername>/<path:filename>')
def serve_file2(foldername, filename):
    folder_path = folderpath
    if foldername:
        folder_path = os.path.join(folder_path, foldername)
    return send_from_directory(folder_path, filename, as_attachment=False)

@app.route('/launch-program')
def launch_program():

    return redirect('/sudopwd')

@app.route('/sudopwd', methods=['GET', 'POST'])
def sudopwd():
    if request.method == 'POST':
        password = request.form['sudopwd']

        # Set the sudo password in the session
        session['sudopwd'] = password

        return redirect('/execute-command')

    return render_template('sudopwd.html')

@app.route('/execute-command')
def execute_command():
    if 'sudopwd' not in session:
        return redirect('/sudopwd')

    folder_path = folderpath
    command1 = ['sudo', 'rsync', '-avz', '--chmod=750', '/home/darnahi/admin/files/Darnahi', f'{folder_path}']
    command2 = ["curl", "-u", f"{user}:{pwd}", "-T", f"{folder_path}", f"{nextcloud_url}" ]

    password = session.get('sudopwd', '')

    try:
        process1 = subprocess.Popen(
            command1,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )
        output, error = process1.communicate(input=password + '\n')

        if process1.returncode != 0:
            return "Unable to run due to non-superuser status!"
            
        for filename in os.listdir(f'{folder_path}'):
            file_path = os.path.join(f'{folder_path}', filename)
            if os.path.isfile(file_path):
                process2 = subprocess.Popen(
                    command2,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    universal_newlines=True
                )
                process2.communicate()
            
        return "Program launched successfully!"
    except subprocess.CalledProcessError as e:
        return "Error occurred while running the Sync! Login directly to continue."



@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if 'logged_in' not in session:
        return redirect('/login')
    
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename =file.filename
            file.save(os.path.join(folderpath. filename))
            return 'File uploaded successfully!'
    return render_template('upload.html')

@app.route('/connect_nc')
def connect_nc():
    if 'logged_in' not in session:
        return redirect('/login')

    return render_template('connect_nc.html')

@app.errorhandler(404)
def page_not_found(error):
    print("Error 404 Encountered")
    return render_template('error.html', error_message='Page not found'), 404

if __name__== '__main__':
    app.run('0.0.0.0', port=3001)
    print("server is running at http://localhost:3001")
