'''create 3 classes that model how a printer could take print jobs out of a print queue
Requirements:
- Printqueue class that follows the queue data structure implementation
- Job class - page attribute each job can have random 1 to 10
            - should also have print_page() method to decrement pages
            - check_complete() which will check if all papers are printed

- printer class - get_job() - account for the case where printqueue.items is empty
                - print_job()


'''
import random

class PrintQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        return self.items.insert(0, item)  # save the end of the list for popping

    def dequeue(self):

        if self.items:
            return self.items.pop()
        else:
            return None
    def size(self):
        print(f'Size of the queue: {len(self.items)}')
        return len(self.items)

    def is_empty(self):
        return self.items == []

class Job:
    def __init__(self):
        self.pages = random.randint(1, 11)

    def print_page(self):
        if self.pages > 0:
            self.pages -= 1

    def check_complete(self):
        if self.pages == 0:
            return True
        return False

class Printer:
    def __init__(self):
        self.current_job = None

    def get_job(self, print_queue):
        try:
            self.current_job = print_queue.dequeue()
        except IndexError:
            return "No more jobs to print"

    def print_job(self, job):
        while job.pages > 0:
            job.print_page()

        if job.check_complete():
            return "Printing Complete"
        else:
            return 'An error occured.'
if __name__ == '__main__':
    job = Job()
    print_queue = PrintQueue()
    printer = Printer()
    print_queue.enqueue(job)
    print(print_queue.items)
    printer.get_job(print_queue)
    print(print_queue.items)
    print(printer.print_job(printer.current_job))