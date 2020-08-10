import cv2
import numpy as np
import image_analyzer.image_markers as markers

class Generator:

    def generate(self, markers_qty, small_perif, corners, middle, edges):
        #TODO: dopisac dodawanie innych kształtow w celu definiowania innego targetu
        if small_perif =='simens':
            im_small_perif = cv2.imread("image\simens_star.png")
        elif small_perif =='slanted_edge':
            im_small_perif = cv2.imread("image/slanted_edge_57.png")

        if corners == "slanted_edge":
            im_corners = cv2.imread("image/slanted_edge_57.png")
        elif corners == 'simens':
            im_corners = cv2.imread("image\simens_star.png")

        if middle == "simens":
            im_middle = cv2.imread("image\simens_star.png")
        elif middle == "slanted_edge":
            im_middle = cv2.imread("image/slanted_edge_57.png")

        if edges == "slanted_edge":
            im_edges = cv2.imread("image/slanted_edge_57.png")
        elif edges == "simens":
            im_edges = cv2.imread("image\simens_star.png")


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

            im_corners = cv2.resize(im_corners, (1000, 1000))

            im_edges = cv2.resize(im_edges, (1000, 1000))

            im_middle = cv2.resize(im_middle, (3000, 3000))
            shapeX = im_middle.shape[1]
            shapeY = im_middle.shape[0]

            widthX = int(shapeX/3)
            widthY = int(shapeY/3)

            # imageCut00 = im_middle[0:widthY, 0:widthX]
            # imageCut01 = im_middle[widthY:2 * widthY, 0:widthX]
            # imageCut02 = im_middle[2 * widthY:3 * widthY, 0:widthX]
            #
            # imageCut10 = im_middle[0:widthY, widthX:2 * widthX]
            # imageCut11 = im_middle[widthY:2*widthY, widthX:2*widthX]
            # imageCut12 = im_middle[2 * widthY:3 * widthY, widthX:2 * widthX]
            #
            # imageCut20 = im_middle[0:widthY, 2 * widthX:3 * widthX]
            # imageCut21 = im_middle[widthY:2 * widthY, 2 * widthX:3 * widthX]
            # imageCut22 = im_middle[2*widthY:3*widthY, 2*widthX:3*widthX]

            imageCut00 = im_middle[0:widthX, 0:widthY]
            imageCut01 = im_middle[0:widthX, widthX:2 * widthX]
            imageCut02 = im_middle[0:widthX, 2 * widthY:3 * widthY]

            imageCut10 = im_middle[widthX:2 * widthX, 0:widthY]
            imageCut11 = im_middle[widthX:2 * widthX, widthY:2 * widthY]
            imageCut12 = im_middle[widthX:2 * widthX, 2 * widthY:3 * widthY]

            imageCut20 = im_middle[2 * widthX:3 * widthX, 0:widthY]
            imageCut21 = im_middle[2 * widthX:3 * widthX, widthY:2 * widthY]
            imageCut22 = im_middle[2 * widthX:3 * widthX, 2 * widthY:3 * widthY]


            blank_image = 255 * np.ones(shape=[1000, 1000, 3], dtype=np.uint8)

            # col0 = np.vstack([ms[0], im_small_perif, blank_image, im_edges, blank_image, im_small_perif, ms[1]])
            # col1 = np.vstack([im_small_perif, im_corners, blank_image, blank_image, blank_image, im_corners, im_small_perif])
            # col2 = np.vstack([blank_image, blank_image, imageCut00, imageCut01, imageCut02, blank_image, blank_image])
            # col3 = np.vstack([im_edges, blank_image, imageCut10, imageCut11, imageCut12, blank_image, im_edges])
            # col4 = np.vstack([blank_image, blank_image, imageCut20, imageCut21, imageCut22, blank_image, blank_image])
            # col5 = np.vstack([im_small_perif, im_corners, blank_image, blank_image, blank_image, im_corners, im_small_perif])
            # col6 = np.vstack([ms[2], im_small_perif, blank_image, im_edges, blank_image, im_small_perif, ms[3]])
            #
            # target = np.hstack([col0, col1, col2, col3, col4, col5, col6])

            col0 = np.hstack([ms[0], im_small_perif, blank_image, im_edges, blank_image, im_small_perif, ms[2]])
            col1 = np.hstack([im_small_perif, im_corners, imageCut00, imageCut01, imageCut02, im_corners, im_small_perif])
            col2 = np.hstack([im_edges, blank_image, imageCut10, imageCut11, imageCut12, blank_image, im_edges])
            col3 = np.hstack([im_small_perif, im_corners, imageCut20, imageCut21, imageCut22, im_corners, im_small_perif])
            col4 = np.hstack([ms[1], im_small_perif, blank_image, im_edges, blank_image, im_small_perif, ms[3]])

            target = np.vstack([col0, col1, col2, col3, col4])

            #cv2.imwrite('../output/target.png', target)
            cv2.imwrite('../output/target_7x5.png', target)


        elif markers_qty == 6:
            pass
        elif markers_qty == 8:
            pass
        else:
            raise AttributeError('Markers_qty can be equal only to 4, 6 or 8')

if __name__ == "__main__":
    target = Generator()
    target.generate(markers_qty=4, small_perif='simens', corners='slanted_edge', middle='simens', edges='slanted_edge')