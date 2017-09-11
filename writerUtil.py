import csv
import math

def writerF(currentAngle, Goal, carX, carY):
    with open('carlog.csv', 'a+') as csvfile:
        angle = math.atan2(math.sin(math.radians(currentAngle)), math.cos(math.radians(currentAngle)))
        dist = math.sqrt((Goal[0] - carX)**2 + (Goal[1] - carY)**2)
        alpha = math.atan2(Goal[0] - carX, Goal[1] - carY)
        #error = math.anglediff(angle, alpha)
        spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([angle, dist, alpha, carX, carY, Goal[0], Goal[1]])
       # spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])