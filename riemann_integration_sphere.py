from math import sqrt, pi

def partition_length(sphere_radius, partition):
    return sphere_radius/partition

def x_value(sphere_radius, partition, index):
    """
    Formula to determine the x value, which will be the radius of the circle at points in the hemisphere
    """

    return partition_length(sphere_radius, partition) * index

def y_value(sphere_radius, circle_radius):
    """
    Formula for a semicircle: sqrt(radius**2 - x**2)
    """
    return sqrt(sphere_radius**2 - circle_radius**2)

def area_of_a_circle(sphere_radius, partition, index):
    """
    Formula for area of a circle
    """
    circle_radius = x_value(sphere_radius, partition, index)

    return pi * circle_radius**2

def height_of_cyclinder(sphere_radius, partition, index):
    """
    To determine the height of the cyclinder we have to find the distance between f(x1) and f(x2) where x1 and x2 are in the partition
    """
    radius1 = x_value(sphere_radius, partition, index)
    radius2 = x_value(sphere_radius, partition, index-1)

    return abs(y_value(sphere_radius, radius1) - y_value(sphere_radius, radius2))

def volume_of_cyclinder(sphere_radius, partition, index):
    """
    Formula for the volume of a sphere
    """

    area = area_of_a_circle(sphere_radius, partition, index)
    height = height_of_cyclinder(sphere_radius, partition, index)

    return area * height

def my_summation(sphere_radius, partition):
    volume = 0
    for i in range(1, partition+1):
        volume += volume_of_cyclinder(sphere_radius, partition, i)
    return volume

def main():
    while True:
        radius = int(input("Enter radius of the hemisphere: "))
        partition = int(input("Enter how many partitions you want: "))

        print(2*my_summation(radius, partition))
        print(4/3 * pi * radius**3)
        
        input()

if __name__ == "__main__":
    main()