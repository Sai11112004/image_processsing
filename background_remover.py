import cv2
import mediapipe as mp
import numpy as np

mp_selfie_segmentation = mp.solutions.selfie_segmentation
segmentor = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)

image = cv2.imread("backremover1.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

results = segmentor.process(image_rgb)
mask = results.segmentation_mask > 0.5

bg_removed = np.where(mask[..., None], image, (255, 255, 255)).astype(np.uint8)
cv2.imwrite("output_no_bg.jpg", bg_removed)
