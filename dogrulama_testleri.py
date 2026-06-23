import time

class DogrulamaTestleri:
    def __init__(self):
        self.queue = []
        self.verified_data = []

    def add_to_queue(self, data):
        """Adds incoming data to validation queue."""
        print(f"Data added to validation queue: {data}")
        self.queue.append(data)

    def process_queue(self):
        """Process and validate incoming data."""
        if not self.queue:
            print("Validation queue is empty.")
            return

        print("Processing validation queue...")
        while self.queue:
            item = self.queue.pop(0)
            time.sleep(0.1) # Simulate processing time
            print(f"Validating item: {item}")
            # Here we simulate successful validation logic
            self.verified_data.append(item)

        print("All data in queue has been validated.")

    def get_verified_data(self):
        return self.verified_data

if __name__ == "__main__":
    validator = DogrulamaTestleri()
    validator.add_to_queue({"test": "data", "value": 6.52})
    validator.process_queue()
