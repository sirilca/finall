import threading
import subprocess

# Define a function to run a Python file as a subprocess
def run_file(file_path):
    subprocess.call(["python", file_path])

# Create two threads to run the Python files concurrently
thread1 = threading.Thread(target=run_file, args=("game_1\\camera.py",))
thread2 = threading.Thread(target=run_file, args=("game_1\\game.py",))

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()
