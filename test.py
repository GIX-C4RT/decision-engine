import rospy
from geometry_msgs.msg import Pose, PoseStamped

rospy.init_node('tt', anonymous=True)
pub = rospy.Publisher('move_base_simple/goal', PoseStamped, latch=True, queue_size=10)
NavGoal = PoseStamped()
NavGoal.header.frame_id = "map"
NavGoal.header.stamp = rospy.Time.now()
# NavGoal.pose = target_pose
NavGoal.pose = Pose()
# while True:
pub.publish(NavGoal)