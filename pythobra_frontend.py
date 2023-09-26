import sys
import PySide6.QtWidgets as QW
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtGui import QMovie
import webbrowser


class PythobraMainWindow(QW.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pythobra")
        main_widget = QW.QWidget()
        self.setCentralWidget(main_widget)
        vertical_layout = QW.QVBoxLayout()
        horizontal_layout = QW.QHBoxLayout()
        main_widget.setLayout(vertical_layout)

        vertical_layout.addLayout(horizontal_layout)

        equation_label = QW.QLabel("Equation: ")
        horizontal_layout.addWidget(equation_label)

        self.equation_text_field = QW.QLineEdit()
        horizontal_layout.addWidget(self.equation_text_field)

        variable_label = QW.QLabel("Solve for: ")
        horizontal_layout.addWidget(variable_label)

        self.variable_text_field = QW.QLineEdit()
        horizontal_layout.addWidget(self.variable_text_field)

        self.solve_equation_button = QW.QPushButton("Solve equation")
        horizontal_layout.addWidget(self.solve_equation_button)

        horizontal_layout_2 = QW.QHBoxLayout()
        vertical_layout.addLayout(horizontal_layout_2)

        output_label = QW.QLabel("Output")
        horizontal_layout_2.addWidget(output_label)

        horizontal_layout_2.addStretch()

        self.settings_button = QW.QPushButton("Settings")
        horizontal_layout_2.addWidget(self.settings_button)

        self.output_text_field = QW.QPlainTextEdit()
        self.output_text_field.setReadOnly(True)
        vertical_layout.addWidget(self.output_text_field)


class SettingsDialog(QW.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.vertical_layout = QW.QVBoxLayout()
        self.setLayout(self.vertical_layout)
        settings_movie = QMovie("img/settings.gif")
        settings_label = QW.QLabel()
        settings_label.setMovie(settings_movie)
        settings_movie.start()
        self.vertical_layout.addWidget(settings_label)
        self.vertical_layout.addWidget(
            QW.QLabel(
                "You got Rickrolled! You better read the source code before blindly running any code!"
            )
        )
        button_box = QW.QDialogButtonBox(
            QW.QDialogButtonBox.Ok | QW.QDialogButtonBox.Cancel
        )
        self.vertical_layout.addWidget(button_box)

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        webbrowser.open(
            "https://ia801509.us.archive.org/10/items/Rick_Astley_Never_Gonna_Give_You_Up/Rick_Astley_Never_Gonna_Give_You_Up.ogv"
        )
