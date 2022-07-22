fig, axs = plt.subplots(nrows=5, ncols=5, figsize = (100,100))
# fig.tight_layout()


lower = (5, 20, 40)
upper = (100,255,255)
kernel = np.ones((3, 3), np.uint8)
i = 0
for img, conf_ in copy.deepcopy(zip(imgs, confs_)):
    ax = plt.subplot(5, 5, i + 1)

    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_img, lower, upper)
    
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=1)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    filtered_cnt = []
    min_area = 40 * 50

    for cnt in contours[1:]:
        area = cv2.contourArea(cnt)
        if area > min_area:
            filtered_cnt.append(cnt)

    print(img.shape[:2])
    
    for cnt in filtered_cnt:
        max_x = img.shape[1]
        leftmost = None
        for point in cnt:

            if max_x > point[0][0]:
                max_x = point[0][0]
                leftmost = point[0]

        cv2.circle(img, leftmost, 10, (255, 255,0 ), -1)

    cv2.drawContours(img, delimiters, -1, (255,0,0), 3)
    
    plt.imshow(img)
    plt.title(f"{i}:\n" + conf_)
    
    i += 1