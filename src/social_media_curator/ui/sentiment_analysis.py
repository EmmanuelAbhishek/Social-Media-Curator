import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton,
    QTextEdit, QFileDialog, QMessageBox, QTableWidget, QTableWidgetItem
)
from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        # Initialize the Hugging Face sentiment analysis pipeline
        self.analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

    def analyze_text(self, text):
        try:
            result = self.analyzer(text)
            label = result[0]['label']
            score = result[0]['score']
            return label, round(score * 100, 2)
        except Exception as e:
            return f"Error: {str(e)}", 0.0

    def analyze_batch(self, texts):
        results = []
        for text in texts:
            label, score = self.analyze_text(text)
            results.append((text, label, score))
        return results


class SentimentAnalysisApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enhanced Sentiment Analyzer")
        self.setGeometry(100, 100, 800, 600)

        self.analyzer = SentimentAnalyzer()

        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Components
        self.instruction_label = QLabel("Enter text(s) for analysis (one per line):")
        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText("Type or paste text here...")

        self.analyze_button = QPushButton("Analyze Sentiment")
        self.analyze_button.clicked.connect(self.analyze_sentiment)

        self.upload_button = QPushButton("Upload Text File")
        self.upload_button.clicked.connect(self.upload_file)

        self.result_table = QTableWidget()
        self.result_table.setColumnCount(3)
        self.result_table.setHorizontalHeaderLabels(["Text", "Sentiment", "Confidence (%)"])
        self.result_table.horizontalHeader().setStretchLastSection(True)

        # Add components to layout
        layout.addWidget(self.instruction_label)
        layout.addWidget(self.text_input)
        layout.addWidget(self.analyze_button)
        layout.addWidget(self.upload_button)
        layout.addWidget(self.result_table)

    def analyze_sentiment(self):
        input_text = self.text_input.toPlainText()
        if not input_text.strip():
            QMessageBox.warning(self, "Input Error", "Please enter text for analysis.")
            return

        texts = input_text.strip().split("\n")
        results = self.analyzer.analyze_batch(texts)

        self.result_table.setRowCount(0)  # Clear previous results
        for row, (text, label, score) in enumerate(results):
            self.result_table.insertRow(row)
            self.result_table.setItem(row, 0, QTableWidgetItem(text))
            self.result_table.setItem(row, 1, QTableWidgetItem(label))
            self.result_table.setItem(row, 2, QTableWidgetItem(f"{score}%"))

    def upload_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Text File", "", "Text Files (*.txt);;All Files (*)")
        if not file_path:
            return

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read().strip()
            self.text_input.setPlainText(content)
        except Exception as e:
            QMessageBox.critical(self, "File Error", f"Failed to read file: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SentimentAnalysisApp()
    window.show()
    sys.exit(app.exec_())
