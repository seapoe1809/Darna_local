##Sets up the flask server for viewing the folder locally at {ip_address}:3001
from flask import Flask, render_template, send_from_directory, session, request, redirect
from urllib.parse import quote, unquote
import webbrowser
import os, subprocess
import getpass
import variables
import qrcode



app = Flask(__name__)
app.secret_key = 'your_secret_key_jjkjdhbclskdbvlkdfv'

#importing variables from variables.py
HS_path = variables.HS_path
ocr_files = variables.ocr_files
upload_dir = variables.upload_dir
folderpath = variables.Health_files
ip_address = variables.ip_address

# Configure static folder path
app.static_folder = 'static'


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

    files = os.listdir(folder_path)
    file_links = []

    for filename in files:
        file_path = os.path.join(folder_path, filename)
        is_directory = os.path.isdir(file_path)

        if is_directory:
            if foldername:
                file_links.append({'filename': filename, 'path': f'/folder/{foldername}/{filename}/', 'is_folder': True})
            else:
                file_links.append({'filename': filename, 'path': f'/folder/{filename}/', 'is_folder': True})
        else:
            if foldername:
                file_links.append({'filename': filename, 'path': f'/folder/{foldername}/{filename}', 'is_folder': False})
            else:
                file_links.append({'filename': filename, 'path': f'/{filename}', 'is_folder': False})

    return render_template('folder_index.html', files=file_links)

@app.route('/<path:filename>')
def serve_file(filename):
    if 'logged_in' not in session:
        return redirect('/login')

    decoded_filename = unquote(filename)
    return send_from_directory(folderpath, decoded_filename, as_attachment=False)


@app.route('/folder/<path:foldername>/<path:filename>')
def serve_file2(foldername, filename):
    if 'logged_in' not in session:
        return redirect('/login')

    folder_path = os.path.join(folderpath, foldername)
    decoded_filename = unquote(filename)
    return send_from_directory(folder_path, decoded_filename, as_attachment=False)


@app.route('/launch-program')
def launch_program():
    return redirect('/sudopwd')

@app.route('/sudopwd', methods=['GET', 'POST'])
def sudopwd():
    if request.method == 'POST':
        password1 = request.form['sudopwd']

        # Set the sudo password in the session
        session['sudopwd'] = password1

        return redirect('/execute-command')

    return render_template('sudopwd.html')

@app.route('/execute-command')
def execute_command():
    if 'sudopwd' not in session:
        return redirect('/sudopwd')

    command1 = ['sudo', '-S', 'rsync', '-avz', '--chmod=750']
    source_dir = upload_dir
    destination_dir1 = ocr_files
    destination_dir2 = folderpath
    files_to_rsync = []
    
    password1 = session.get('sudopwd', '')
    
        
    # Rsyncing files to parent directory, fist code to execute
    command1_all_files = ['sudo', '-S', 'rsync', '-avz', '--chmod=750', f"{upload_dir}/", f"{folderpath}/"]
    try:
        process_all_files_sync=subprocess.Popen(
           command1_all_files,
           stdin=subprocess.PIPE,
           stdout=subprocess.PIPE,
           universal_newlines=True
        )
        output, error = process_all_files_sync.communicate(input=password1 + '\n')
        if process_all_files_sync.returncode != 0:
            return "Unable to run due to non-superuser status!"
    except subprocess.CalledProcessError as e:
        return "Error occurred while clearing files in the upload directory."   
    # setting up to Sync select files to ocr_files directory
    

    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        if os.path.isfile(file_path) and any(filename.endswith(ext) for ext in ['.pdf', '.png', '.jpg', '.txt', '.jpeg']):
            files_to_rsync.append(file_path)

    if not files_to_rsync:
        return "No files to synchronize!"

    command1.extend(files_to_rsync)
    command1.append(destination_dir1)
    #running rsync part 2 code to sync with ocr-dir
    try:
        process1 = subprocess.Popen(
            command1,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )
        output, error = process1.communicate(input=password1 + '\n')

        if process1.returncode != 0:
            return "Unable to run due to non-superuser status!"

    except subprocess.CalledProcessError as e:
        return "Error occurred while running rsync command for file synchronization."
        
    #running caffeine to keep computed awake
    command2 = ['caffeine']
    try:
        process2 = subprocess.Popen(command2)
    except subprocess.CalledProcessError as e:
        return "Error occurred while running caffeine."
    
    #setting up to run apple health grafana
    command3 = ['sudo', '-S', 'docker-compose', '-f', 'apple-health-grafana/docker-compose.yml', '-p', 'apple-health-grafana', 'pull']
    command4 = ['sudo', '-S', 'docker-compose', '-f', 'apple-health-grafana/docker-compose.yml', '-p', 'apple-health-grafana', 'up', '-d', 'grafana', 'influx']
    command5 = ['sudo', '-S', 'docker-compose', '-f', 'apple-health-grafana/docker-compose.yml', '-p', 'apple-health-grafana', 'up', 'ingester']
    

    try:
        export_zip_path = os.path.join(source_dir, 'export.zip')
        if os.path.isfile(export_zip_path):
            process3 = subprocess.Popen(
                command3,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                universal_newlines=True
            )
            output, error = process3.communicate(input=password1 + '\n')

            process4 = subprocess.Popen(
                command4,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                universal_newlines=True
            )
            output, error = process4.communicate(input=password1 + '\n')

            process5 = subprocess.run(command5, check=True)
            

    except subprocess.CalledProcessError as e:
        return "Error occurred while running Grafana Docker commands."
     
    #running command 6 to clear files in upload dir
    command6 = f'rm -rf {source_dir}/*'
    try:
        process6 = subprocess.run(command6, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        return "Error occurred while clearing files in the upload directory."

    return "Programs launched successfully! Clearing files in the upload directory."


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if 'logged_in' not in session:
        return redirect('/login')
    
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename =file.filename
            file.save(os.path.join(upload_dir, filename))
            return 'File uploaded successfully!'
    return render_template('upload.html')

@app.route('/connect_nc')
def connect_nc():
    if 'logged_in' not in session:
        return redirect('/login')
    url = "http://192.168.99.245:3001"
    qr = qrcode.QRCode()
    qr.add_data(url)
    qr.make()
    image = qr.make_image()
    image.save(f'{HS_path}/static/qrcode.png')
    return render_template('connect_nc.html')
    
@app.route('/apple_view')
def apple_view():
    if 'logged_in' not in session:
        return redirect('/login')
        
    url2 = f"http://{ip_address}:3000"
    
    return redirect(url2)


@app.errorhandler(404)
def page_not_found(error):
    print("Error 404 Encountered")
    return render_template('error.html', error_message='Page not found'), 404

if __name__== '__main__':
    app.run('0.0.0.0', port=3001)
    print("server is running at http://localhost:3001")
