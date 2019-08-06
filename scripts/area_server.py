#!/usr/bin/env python

import rospy
from ros_service_assignment.srv import RectangleAreaService
from ros_service_assignment.srv import RectangleAreaServiceRequest
from ros_service_assignment.srv import RectangleAreaServiceResponse


def handle_area(req):
    print("Print [%s * %s] = %s" % (req.a, req.b, (req.a*req.b)))
    return RectangleAreaServiceResponse(req.a*req.b)


def area_server():
    rospy.init_node('area_server')
    s = rospy.Service('area_service', RectangleAreaService, handle_area)
    print("Ready to calculate area")
    rospy.spin()


if __name__ == '__main__':
    area_server()
