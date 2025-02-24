# Without Design Pattern
class Report:
    def generate_report(self, report_type):
        if report_type == "pdf":
            print("Generating PDF report: Header")
            print("Generating PDF report: Data")
            print("Generating PDF report: Footer")
        elif report_type == "csv":
            print("Generating CSV report: Header")
            print("Generating CSV report: Data")
            print("Generating CSV report: Footer")

report_pdf = Report()
report_csv = Report()

report_pdf.generate_report("pdf")
report_csv.generate_report("csv")

# With Design Pattern
from abc import ABC, abstractmethod

class ReportGenerator(ABC):
    def generate_report(self):
        self.generate_header()
        self.generate_data()
        self.generate_footer()

    @abstractmethod
    def generate_header(self):
        pass

    @abstractmethod
    def generate_data(self):
        pass

    @abstractmethod
    def generate_footer(self):
        pass

class PDFReportGenerator(ReportGenerator):
    def generate_header(self):
        print("Generating PDF report: Header")

    def generate_data(self):
        print("Generating PDF report: Data")

    def generate_footer(self):
        print("Generating PDF report: Footer")

class CSVReportGenerator(ReportGenerator):
    def generate_header(self):
        print("Generating CSV report: Header")

    def generate_data(self):
        print("Generating CSV report: Data")

    def generate_footer(self):
        print("Generating CSV report: Footer")

report_pdf = PDFReportGenerator()
report_csv = CSVReportGenerator()

report_pdf.generate_report()
report_csv.generate_report()