
# 🎨 AI-Comic-Studio

A simple **PyQt5-based desktop application** that uses a Stable Diffusion model to generate comic-style images from text prompts. Built with 🤗 Hugging Face's `diffusers` library and PyTorch, this tool allows you to customize inference steps and save your generated panels easily.

---

## 🖼️ Demo

![demo](test.jpg) <!-- Optional: Add a screenshot -->

---

## 🚀 Features

- ✏️ Enter custom prompts to generate comic panels.
- ⚙️ Adjust the number of inference steps for fine-tuning output quality.
- 🖼️ View generated images directly in the GUI.
- 💾 Save your favorite panels as PNG images.

---

## 🧠 Model

This app uses the [Lykon/dreamshaper-7](https://huggingface.co/Lykon/dreamshaper-7) Stable Diffusion model, known for producing high-quality, artistic outputs.

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-comic-studio.git
cd ai-comic-studio
````

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🧪 Running the App

```bash
python comic_generator_gui.py
```

---

## 📝 Usage Instructions

1. Enter a prompt (e.g., `comic panel, superhero flying through city, dramatic lighting`).
2. Adjust the inference steps (default is 30).
3. Click **"Generate Comic Panel"**.
4. View the result in the GUI.
5. Click **"Save Image"** to export it as a PNG.

---

## 📂 Project Structure

```
ai-comic-studio/
├── comic_generator_gui.py       # Main application code
├── requirements.txt             # Python dependencies
├── demo_screenshot.png          # Optional demo image
└── README.md
```

---

## ⚠️ Notes

* A CUDA-compatible GPU is recommended for faster image generation.
* The model is downloaded from Hugging Face on the first run and then cached locally.
* Internet connection is required on first launch to fetch model weights.

---

## 📃 License

This project is licensed under the **MIT License**.

---

## ⭐️ Support the Project

If you find this project helpful, consider giving it a ⭐️ on [GitHub](https://github.com/your-username/ai-comic-studio)!

---

## 🙌 Acknowledgments

* [Hugging Face Diffusers](https://github.com/huggingface/diffusers)
* [Lykon/dreamshaper-7](https://huggingface.co/Lykon/dreamshaper-7)
* [PyTorch](https://pytorch.org/)
* [PyQt5](https://riverbankcomputing.com/software/pyqt/intro)

```

---


Let me know if you'd like a badge section (for things like Python version, license, etc.) or a GitHub Actions CI workflow example.
```
