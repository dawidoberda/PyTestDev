import cv2
import numpy as np
import image_analyzer.image_markers as markers

class Generator:

    def generate(self, markers_qty):
        m = markers.Marker()
        for i in range(markers_qty):
            m.generate_marker(i)
            m.save_marker(f"tmp/marker{i}")

if __name__ == "__main__":
    target = Generator()
    target.generate(markers_qty=4)