import sys
import torch
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QTextEdit, QPushButton,
    QVBoxLayout, QFileDialog, QSpinBox, QHBoxLayout
)
from PyQt5.QtGui import QPixmap, QImage
from diffusers import StableDiffusionPipeline

class ComicGeneratorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Comic Generator")
        self.setGeometry(200, 200, 650, 650)

        layout = QVBoxLayout()

        # Prompt input
        self.prompt_label = QLabel("Enter Prompt:")
        layout.addWidget(self.prompt_label)

        self.prompt_input = QTextEdit()
        self.prompt_input.setPlaceholderText("Example: comic panel, superhero fighting villain, vibrant colors")
        layout.addWidget(self.prompt_input)

        # Inference steps control
        steps_layout = QHBoxLayout()
        steps_label = QLabel("Inference Steps:")
        self.steps_spin = QSpinBox()
        self.steps_spin.setRange(5, 100)
        self.steps_spin.setValue(30)  # Default
        steps_layout.addWidget(steps_label)
        steps_layout.addWidget(self.steps_spin)
        layout.addLayout(steps_layout)

        # Generate button
        self.generate_btn = QPushButton("Generate Comic Panel")
        self.generate_btn.clicked.connect(self.generate_comic)
        layout.addWidget(self.generate_btn)

        # Image display
        self.image_label = QLabel("Generated Image will appear here")
        layout.addWidget(self.image_label)

        # Save button
        self.save_btn = QPushButton("Save Image")
        self.save_btn.clicked.connect(self.save_image)
        self.save_btn.setEnabled(False)
        layout.addWidget(self.save_btn)

        self.setLayout(layout)

        # Load SD pipeline once
        MODEL_ID = "Lykon/dreamshaper-7"
        print("[INFO] Loading model:", MODEL_ID)

        self.pipe = StableDiffusionPipeline.from_pretrained(
            MODEL_ID,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
        )
        if torch.cuda.is_available():
            self.pipe = self.pipe.to("cuda")

        self.generated_image = None

    def generate_comic(self):
        prompt = self.prompt_input.toPlainText().strip()
        if not prompt:
            self.image_label.setText("⚠️ Please enter a prompt first.")
            return

        steps = self.steps_spin.value()
        self.image_label.setText(f"⏳ Generating... ({steps} steps)")

        # Run diffusion
        image = self.pipe(
            prompt,
            negative_prompt="blurry, distorted, watermark, text",
            guidance_scale=7.5,
            num_inference_steps=steps
        ).images[0]

        self.generated_image = image

        # Convert PIL to QPixmap for display
        image = image.convert("RGB")
        data = image.tobytes("raw", "RGB")
        qimage = QImage(data, image.width, image.height, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        self.image_label.setPixmap(pixmap.scaled(512, 512))

        self.save_btn.setEnabled(True)

    def save_image(self):
        if self.generated_image:
            filepath, _ = QFileDialog.getSaveFileName(self, "Save Image", "comic_output.png", "PNG Files (*.png)")
            if filepath:
                self.generated_image.save(filepath)
                self.image_label.setText(f"✅ Saved to {filepath}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ComicGeneratorGUI()
    window.show()
    sys.exit(app.exec_())
