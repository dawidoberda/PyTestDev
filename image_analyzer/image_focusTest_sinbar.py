import numpy as np
import cv2
import math
import matplotlib.pyplot as plt

class SinBar_focus:

    def mtf(self):
        object = cv2.imread("image/Lenstarg_50_7086p_15g_25is.png")
        object_gray = cv2.cvtColor(object, cv2.COLOR_BGR2GRAY)

        y_dim, x_dim = object_gray.shape
        print(f'y_dim = {y_dim}')
        print(f'x_dim = {x_dim}')

        measure_line = int(y_dim/2) - 200

        #OBJECT PROCESSING
        contrast_object = []

        for x in range(1, x_dim-10, 1):
            c = object_gray[measure_line, x]
            cv2.circle(object, (x, measure_line), 1, (0, 0, 255), 1, 1)  # for debug
            contrast_object.append(c)

        contrast_object = np.array(contrast_object, dtype=int)
        print(contrast_object)

        #For debug - simulate Image
        image = cv2.GaussianBlur(object, (15,15), 0)
        image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


        #IMAGE PROCESSING
        contrast_image = []

        for x in range(1, x_dim - 10, 1):
            ci = image_grey[measure_line, x]
            cv2.circle(image, (x, measure_line), 1, (0, 0, 255), 1, 1)  # for debug
            contrast_image.append(ci)

        contrast_image = np.array(contrast_image, dtype=int)
        print(contrast_image)

        #TODO: zrobic sygnal odp za sfr na podstawie log z tej strony nowej
        sfr_min = 2 #[lp/mm]
        sfr_max = 200 #[lp/mm]

        xmax = x_dim - 10

        for x in range(1, xmax, 1):
            pass



        plt.figure(1)
        plt.plot(contrast_object)
        plt.title("Contrast Object")
        plt.xlabel("Position")
        plt.ylabel('Contrast')
        plt.savefig("../output/bar_object_contrast")

        plt.figure(2)
        plt.plot(contrast_image)
        plt.title("Contrast Image")
        plt.xlabel("Position")
        plt.ylabel('Contrast')
        plt.savefig("../output/bar_image_contrast")


        plt.show()

        cv2.imwrite('tmp/bar_tmp.png', object)
        cv2.imwrite('tmp/bar_image_tmp.png', image)

        # cv2.imshow("target", image)
        # key = cv2.waitKey(0)
        # cv2.destroyAllWindows()


if __name__ == "__main__":
    sinbar = SinBar_focus()
    sinbar.mtf()