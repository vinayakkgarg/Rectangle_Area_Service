#!/usr/bin/env python

import rospy
import sys
from ros_service_assignment.srv import RectangleAreaService
from ros_service_assignment.srv import RectangleAreaServiceRequest
from ros_service_assignment.srv import RectangleAreaServiceResponse


def area_client(x, y):
    rospy.wait_for_service('area_service')
    try:
        area = rospy.ServiceProxy('area_service', RectangleAreaService)
        resp1 = area(x, y)
        return resp1.area
    except rospy.ServiceException, e:
        print("Service call failed : %s" % e)


def usage():
    return "%s [x y]" % sys.argv[0]


if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print("requesting %s * %s" % (x, y))
    s = area_client(x, y)
    print("%s * %s = %s" % (x, y, s))
