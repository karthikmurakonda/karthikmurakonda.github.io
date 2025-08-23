#!/usr/bin/env python3
"""
Generate a clean 'K' favicon for personal branding
"""

try:
    from PIL import Image, ImageDraw, ImageFont
    import os
except ImportError:
    print("PIL (Pillow) is required. Install with: pip install Pillow")
    exit(1)

def create_k_favicon():
    # Create a 32x32 image with white background
    img = Image.new('RGB', (32, 32), color='white')
    draw = ImageDraw.Draw(img)
    
    # Try to use a clean font, fallback to default
    try:
        # Try to find a good system font
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
    except:
        try:
            font = ImageFont.truetype("arial.ttf", 20)
        except:
            font = ImageFont.load_default()
    
    # Calculate text position to center the 'K'
    bbox = draw.textbbox((0, 0), 'K', font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (32 - text_width) // 2
    y = (32 - text_height) // 2 - 2  # Slight adjustment for better centering
    
    # Draw the letter K in dark color
    draw.text((x, y), 'K', fill='#333333', font=font)
    
    # Save the favicon
    output_path = 'static/images/favicon.png'
    img.save(output_path)
    print(f"Favicon saved to {output_path}")
    
    # Also create a 16x16 version for better scaling
    img_small = img.resize((16, 16), Image.Resampling.LANCZOS)
    img_small.save('static/images/favicon-16.png')
    print("16x16 version saved to static/images/favicon-16.png")

if __name__ == "__main__":
    create_k_favicon()
