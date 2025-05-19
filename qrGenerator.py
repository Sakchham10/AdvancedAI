import qrcode
from typing import Optional
from urllib.parse import urlparse

def generate_qr_code(url: str, output_file: str = "qrcode.png") -> None:
    """
    Generate a QR code for the given URL and save it to a file.
    
    Args:
        url (str): The URL to encode in the QR code
        output_file (str): The name of the output file (default: "qrcode.png")
    
    Raises:
        ValueError: If the URL is invalid or empty
    """
    # Validate URL
    if not url:
        raise ValueError("URL cannot be empty")
    
    try:
        parsed_url = urlparse(url)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            raise ValueError("Invalid URL format")
    except Exception as e:
        raise ValueError(f"Invalid URL: {str(e)}")

    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code (1 is 21x21)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code
        border=4,  # Thickness of the border (minimum is 4)
    )
    
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image to a file
    img.save(output_file)
    print(f"QR Code saved as {output_file}")

if __name__ == "__main__":
    try:
        url = input("Enter the URL to generate QR code: ").strip()
        generate_qr_code(url)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")