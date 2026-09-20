import cv2


def process_image(image_path):

    image = cv2.imread(image_path)

    if image is None:
        return 0, None

    # Resize image
    image = cv2.resize(image, (600, 400))

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Remove noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect dark regions
    _, threshold = cv2.threshold(
        blur,
        80,
        255,
        cv2.THRESH_BINARY_INV
    )

    # Calculate damaged area
    total_pixels = threshold.shape[0] * threshold.shape[1]
    damaged_pixels = cv2.countNonZero(threshold)

    damage_percentage = (
        damaged_pixels / total_pixels
    ) * 100

    return damage_percentage, threshold