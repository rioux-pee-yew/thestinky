import os
import cv2
import numpy as np
import torch
from PIL import Image
from depth_anything_3.api import DepthAnything3

# Hide the xFormers warning if you aren't using it
os.environ["XFORMERS_DISABLED"] = "1"

# 1. Select the processing device (GPU if available, otherwise CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# 2. Load the model weights
print("Loading Depth Anything V3 Model...")
model = DepthAnything3.from_pretrained("depth-anything/da3-base")
model = model.to(device=device)

# Added C:/ to make it a true system path
folder_path = "C:/users/rioux/PyCharmMiscProject/depth-anything-3/assets/examples/SOH"
image_filename = "000.png"

image_path = os.path.join(folder_path, image_filename)
print(f"Loading image from: {image_path}")
image = Image.open(image_path).convert("RGB")

# 4. Predict the depth map using V3 API
print("Predicting depth map...")
with torch.no_grad():
    # Pass the image inside a list to model.inference()
    prediction = model.inference([image])

    # Extract the depth map from the output object arrays [index 0]
    depth_map = prediction.depth[0]

# 5. Post-process the depth map for saving
depth_min = depth_map.min()
depth_max = depth_map.max()
if depth_max - depth_min > 0:
    normalized_depth = (depth_map - depth_min) / (depth_max - depth_min)
else:
    normalized_depth = depth_map
normalized_depth = (normalized_depth * 255).astype(np.uint8)

# 6. Save the grayscale depth map
output_gray_path = "output_depth_gray.png"
cv2.imwrite(output_gray_path, normalized_depth)
print(f"Saved grayscale depth map to: {output_gray_path}")

# 7. Apply a colormap (Inferno look) for better visualization
color_depth = cv2.applyColorMap(normalized_depth, cv2.COLORMAP_INFERNO)
output_color_path = "output_depth_color.png"
cv2.imwrite(output_color_path, color_depth)
print(f"Saved colored depth map to: {output_color_path}")

print("Processing Complete!")