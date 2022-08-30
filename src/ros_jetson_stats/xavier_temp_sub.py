#!/usr/bin/env python

import rospy
from diagnostic_msgs.msg import DiagnosticArray, DiagnosticStatus
from std_msgs.msg import Float32

class xavier_temperature(object):
    def _init_(self):
        self.sub = rospy.Subscriber("/diagnostics", DiagnosticArray, self.agg_cb, queue_size=1)
        self.GPU_pub = rospy.Publisher('/GPU_temp', Float32, queue_size=1)
        self.CPU_pub = rospy.Publisher('/GPU_temp', Float32, queue_size=1)
        rospy.loginfo("here3")
        self.GPU_temp = 0
        self.CPU_temp = 0


    def agg_cb(self, msg):
        rospy.loginfo("here")
        for i in enumerate(msg.status):
            if msg.status[i].name == "jetson_stats temp" :
                for j in enumerate(msg.status[i].values):
                    if msg.status[i].values[j].key == "GPU" :
                        self.GPU_temp = msg.status[i].values[j].value
                        self.temp_pub()
                        break
                    if msg.status[i].values[j].key == "CPU" :
                        self.CPU_temp = msg.status[i].values[j].value
                        self.temp_pub()
                        break
                break

    def GPU_temp_pub(self):
        self.GPU_pub.publish(self.GPU_temp)

    def CPU_temp_pub(self):
        self.GPU_pub.publish(self.CPU_temp)

    def spin(self):
        rospy.loginfo("here2")
        rospy.spin()


if __name__ == "__main__":
	rospy.init_node('xavier_temp',anonymous=True)
	xavier_temp = xavier_temperature()
	xavier_temp.spin()
