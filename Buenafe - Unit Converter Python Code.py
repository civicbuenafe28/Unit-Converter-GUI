import sys
from PyQt6.QtWidgets import QApplication, QDialog, QComboBox, QLineEdit, QTextBrowser, QPushButton
from PyQt6.uic import loadUi

class UnitConverter(QDialog):
    def __init__(self):
        super().__init__()
        # Load UI from file
        loadUi("Buenafe - Unit Converter GUI Design.ui", self)

        # Connect signals and slots
        self.ConvertButton = self.findChild(QPushButton, "ConvertButton")
        self.ConvertButton.clicked.connect(self.convert_value)

        # Connect ComboBox objects 
        self.Group1 = self.findChild(QComboBox, "Group1")
        self.Group2 = self.findChild(QComboBox, "Group2")

        # Assuming InputBox and ResultBox 
        self.InputBox = self.findChild(QLineEdit, "InputBox")
        self.ResultBox = self.findChild(QTextBrowser, "ResultBox")
        
        # Set the window title
        self.setWindowTitle("The Unit Converter (Buenafe - M001)") 

    def convert_value(self):
        # Get user input
        input_value = float(self.InputBox.text())
        from_unit = self.Group1.currentText()
        to_unit = self.Group2.currentText()

        try:
            converted_value = convert_units(input_value, from_unit, to_unit)
            converted_value = "{:,.2f}".format(converted_value)
            converted_value += f" {to_unit}"

            # Display the result
            self.ResultBox.setText(f"{converted_value}")
        except ValueError as e:
            self.ResultBox.setText(str(e))


def convert_units(value, from_unit, to_unit):
        conversion_factors = {
            "Fahrenheit to Celsius": lambda x: (x - 32) * 5 / 9,
            "Celsius to Fahrenheit": lambda x: (x * 9 / 5) + 32,
            "Kilometer to Meter": lambda x: x * 1000,
            "Meter to Kilometer": lambda x: x / 1000,
        }

        try:
            conversion_function = conversion_factors[f"{from_unit} to {to_unit}"]
            converted_value = conversion_function(value)
            return converted_value
        except KeyError:
            raise ValueError(f"Invalid unit conversion: {from_unit} to {to_unit}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = UnitConverter()
    converter.show()
    sys.exit(app.exec())
