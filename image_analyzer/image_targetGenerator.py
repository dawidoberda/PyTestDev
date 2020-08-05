import cv2
import numpy as np
import image_analyzer.image_markers as markers

class Generator:

    def generate(self, markers_qty, small_perif, corners):

        if small_perif =='simens':
            im_small_perif = cv2.imread("image\simens_star.png")

        if corners == "slanted_edge":
            im_corners = cv2.imread("image/slanted_edge_57.png")


        if markers_qty ==4:
            m = markers.Marker()
            for i in range(markers_qty):
                m.generate_marker(i,1000)
                m.save_marker(f"tmp/marker{i}")

            ms = []
            for i in range(markers_qty):
                ms.append(cv2.imread(f'tmp\marker{i}.png'))

            for i in range(markers_qty):
                ms[i] = cv2.resize(ms[i], (1000, 1000))

            im_small_perif = cv2.resize(im_small_perif, (1000, 1000))

            blank_image = 255 * np.ones(shape=[1000, 1000, 3], dtype=np.uint8)
            #TODO: dodac corners i middle do obrazu
            col0 = np.vstack([ms[0], im_small_perif, blank_image, blank_image, blank_image, im_small_perif, ms[1]])
            col1 = np.vstack([im_small_perif, blank_image, blank_image, blank_image, blank_image, blank_image, im_small_perif])
            col2 = np.vstack([blank_image, blank_image, blank_image, blank_image, blank_image, blank_image, blank_image])
            col3 = np.vstack([blank_image, blank_image, blank_image, blank_image, blank_image, blank_image, blank_image])
            col4 = np.vstack([blank_image, blank_image, blank_image, blank_image, blank_image, blank_image, blank_image])
            col5 = np.vstack([im_small_perif, blank_image, blank_image, blank_image, blank_image, blank_image, im_small_perif])
            col6 = np.vstack([ms[2], im_small_perif, blank_image, blank_image, blank_image, im_small_perif, ms[3]])

            target = np.hstack([col0, col1, col2, col3, col4, col5, col6])

            cv2.imwrite('../output/target.png', target)


        elif markers_qty == 6:
            pass
        elif markers_qty == 8:
            pass
        else:
            raise AttributeError('Markers_qty can be equal only to 4, 6 or 8')

if __name__ == "__main__":
    target = Generator()
    target.generate(markers_qty=4, small_perif='simens', corners='slanted_edge')