import csv
import math

def writerF(currentAngle, Goal, carX, carY, distList, action):
    with open('carlog.csv', 'a+') as csvfile:
        theta = math.atan2(math.sin(math.radians(currentAngle)), math.cos(math.radians(currentAngle)))
        dist = math.sqrt((Goal[0] - carX)**2 + (Goal[1] - carY)**2)
        alpha = math.atan2(Goal[0] - carX, Goal[1] - carY)
        #error = math.anglediff(theta, alpha)
        error = math.atan2(math.sin(theta - alpha), math.cos(theta - alpha))
        spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([theta, alpha, carX, carY, Goal[0], Goal[1], dist, distList, error, action])