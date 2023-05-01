import threading
import subprocess
import time

# Define a function to run a Python file as a subprocess
def run_file(file_path):
    subprocess.call(["python", file_path])

# Create two threads to run the Python files concurrently
thread1 = threading.Thread(target=run_file, args=("media_control\\medd.py",))
thread2 = threading.Thread(target=run_file, args=("media_control\\gesture.py",))

# Start the threads
thread2.start()
time.sleep(8) # Sleep for 20 seconds
thread1.start()

# Wait for the threads to finish
thread2.join()
thread1.join()
