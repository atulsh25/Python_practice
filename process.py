def run():
    print("Process started running")

def shut_down():
    print("Process stopped")

def start_task():
    print("Task started")

def email_admin():
    print("Violation of the email process")

#the following phase is used to determine the starting point for the execution
if __name__ == '__main__':
    run()
    start_task()
    shut_down()
    email_admin()