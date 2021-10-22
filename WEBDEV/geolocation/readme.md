# Geolocation and javascript
- https://www.w3schools.com/html/tryit.asp?filename=tryhtml5_geolocation

# Finding locations that are close to each other
```
How to group latitude/longitude points that are close to each other
There are a number of ways of determining the distance between two points, but for plotting points on a 2-D graph you probably want the Euclidean distance. If (x1, y1) represents your first point and (x2, y2) represents your second, the distance is
d = sqrt( (x2-x1)^2 + (y2-y1)^2 )
Regarding grouping, you may want to use some sort of 2-D mean to determine how "close" things are to each other. For example, if you have three points, (x1, y1), (x2, y2), (x3, y3), you can find the center of these three points by simple averaging:

```
- https://stackoverflow.com/questions/4349160/how-to-group-latitude-longitude-points-that-are-close-to-each-other#4349271
