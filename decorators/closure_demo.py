def print_message(message):
    def message_sender():
        "Nested Function"
        print(message)
    message_sender()

print_message("Some random message")
