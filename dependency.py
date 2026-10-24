class Printer:
    def print_message(self, message):
        print(message)


class Report:
    def generate(self, printer):
        # The Printer is used temporarily
        printer.print_message("Report generated successfully.")


# Create the objects independently
printer = Printer()
report = Report()

# Report temporarily uses Printer
report.generate(printer)
