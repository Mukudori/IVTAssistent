from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QLabel
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QByteArray
from PyQt5 import Qt
from PyQt5 import QtCore

class ImagePlayer(QWidget):
    def __init__(self, filename, title='', parent=None):
        QWidget.__init__(self, parent)

        # Load the file into a QMovie
        self.movie = QMovie(filename, QByteArray(), self)


        size = self.movie.scaledSize()
        self.setGeometry(150, 150, size.width(), size.height())
        self.setWindowTitle(title)

        self.movie_screen = QLabel()
        # Make label fit the gif
        self.movie_screen.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.movie_screen.setAlignment(QtCore.Qt.AlignCenter)


        # Create the layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.movie_screen)

        self.setLayout(main_layout)

        # Add the QMovie object to the label
        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setSpeed(100)
        self.movie_screen.setMovie(self.movie)
        self.movie.start()