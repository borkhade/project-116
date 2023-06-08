import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img,
             "Sun",
               (20, 300),
                cv2.FONT_HERSHEY_COMPLEX,
                  0.5, (255, 255, 255)
                  )
cv2.putText(img,
             "Mercury", 
             (50, 400),
               cv2.FONT_HERSHEY_SIMPLEX,
                 0.4,
                   (0, 255, 0)
                   )
cv2.putText(img,
             "Venus", 
             (200, 400), 
             cv2.FONT_HERSHEY_SIMPLEX, 
             0.4, 
             (0, 255, 0)
             )
cv2.putText(img,
             "Earth", 
             (350, 400), 
             cv2.FONT_HERSHEY_SIMPLEX,
               0.4,
                 (0, 255, 0)
                 )
cv2.putText(img, 
            "Mars",
              (500, 400), 
              cv2.FONT_HERSHEY_SIMPLEX,
                0.4,
                  (0, 255, 0)
                  )
cv2.putText(img, 
            "Jupiter",
              (650, 400),
                cv2.FONT_HERSHEY_SIMPLEX,
                  0.4, 
                  (0, 255, 0)
                  )
cv2.putText(img,
             "Saturn",
               (800, 400),
                 cv2.FONT_HERSHEY_SIMPLEX, 
                 0.4,
                   (0, 255, 0)
                   )
cv2.putText(img, 
            "Uranus",
              (950, 400),
             cv2.FONT_HERSHEY_SIMPLEX, 
             0.4,
               (0, 255, 0)
               )
cv2.putText(img,
             "Neptune",
               (1100, 400),
                 cv2.FONT_HERSHEY_SIMPLEX,
                   0.4,
                     (0, 255, 0)
                     )
cv2.imshow("output", img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg", img)