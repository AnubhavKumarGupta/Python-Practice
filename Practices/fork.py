import os


def child_process():
    print("Child process. My PID is:", os.getpid())
    # Add the code for the child process here


def parent_process(child_pid):
    print("Parent process. My PID is:", os.getpid())
    print("Child process PID is:", child_pid)
    # Add the code for the parent process here


if __name__ == "__main__":
    # Fork the process
    child_pid = os.fork()

    if child_pid == 0:
        # This code will be executed by the child process
        child_process()
    else:
        # This code will be executed by the parent process
        parent_process(child_pid)
