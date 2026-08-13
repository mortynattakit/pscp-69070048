"""This calculates how much area 2 rectangles are overlapping but if zero then no overlapping"""
x1, y1, w1, h1 = map(int, input().split())
x2, y2, w2, h2 = map(int, input().split())

left1, right1 = x1, x1 + w1
bottom1, top1 = y1, y1 + h1

left2, right2 = x2, x2 + w2
bottom2, top2 = y2, y2 + h2

olw = min(right1, right2) - max(left1, left2)
olh = min(top1, top2) - max(bottom1, bottom2)

if olw > 0 and olh > 0:
    print(olw * olh)
else:
    print("no overlapping")
