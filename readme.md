# 📜 QR Code Generator

A simple Python script that generates a QR code from a given URL using the `qrcode` package.

## 📦 Requirements

* Python 3.x
* [`qrcode`](https://pypi.org/project/qrcode/) (with `pillow` for image handling)

Install the required package with:

```bash
pip install qrcode[pil]
```

## 🚀 Usage

1. Clone the repository or download the script.
2. Run the script:

```bash
python qrcode_generator.py
```

3. When prompted, enter the URL you want to encode into a QR code.
4. The QR code image will be saved as `qrcode.png` in the same directory.

## 🧠 Example

```bash
Enter the URL to generate QR code: https://example.com
QR Code saved as qrcode.png
```

## 🛠️ Customization

You can change the name of the output file or customize the QR code's size, colors, and error correction level inside the script:

```python
generate_qr_code(url, output_file="custom_name.png")
```

## 📂 Output

The script generates a PNG image containing the QR code that links to the provided URL.
