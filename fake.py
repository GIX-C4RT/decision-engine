import sys
import os
import time
import threading
import cv2

from kortex_api.autogen.client_stubs.BaseClientRpc import BaseClient
from kortex_api.autogen.client_stubs.BaseCyclicClientRpc import BaseCyclicClient
from kortex_api.autogen.client_stubs.ControlConfigClientRpc import ControlConfigClient

from kortex_api.autogen.messages import Base_pb2, BaseCyclic_pb2, Common_pb2, ControlConfig_pb2

import utilities

def check_for_end_or_abort(e):
    """Return a closure checking for END or ABORT notifications
    Arguments:
    e -- event to signal when the action is completed
        (will be set when an END or ABORT occurs)
    """
    def check(notification, e = e):
        print("EVENT : " + \
              Base_pb2.ActionEvent.Name(notification.action_event))
        if notification.action_event == Base_pb2.ACTION_END \
        or notification.action_event == Base_pb2.ACTION_ABORT:
            e.set()
    return check

def gripper_close(args):
    with utilities.DeviceConnection.createTcpConnection(args) as router:
        base = BaseClient(router)
        gripper_command = Base_pb2.GripperCommand()
        finger = gripper_command.gripper.finger.add()

        # Close the gripper with position increments
        print("Performing gripper test in position...")
        gripper_command.mode = Base_pb2.GRIPPER_POSITION
        position = 0.00
        finger.finger_identifier = 1
        while position < 0.4:
            finger.value = position
            print("Going to position {:0.2f}...".format(finger.value))
            base.SendGripperCommand(gripper_command)
            position += 0.3
            time.sleep(1)


def pre_grasp(args):
    with utilities.DeviceConnection.createTcpConnection(args) as router:
        base = BaseClient(router)
        base_cyclic = BaseCyclicClient(router)
        control = ControlConfigClient(router)

        # feedback = base_cyclic.RefreshFeedback()
        # print(feedback.base.tool_pose_x, feedback.base.tool_pose_y, feedback.base.tool_pose_z)
        # print(feedback.base.tool_pose_theta_x, feedback.base.tool_pose_theta_y, feedback.base.tool_pose_theta_z)
        action = Base_pb2.Action()
        action.name = "Example Cartesian action movement"
        action.application_data = ""
        cartesian_pose = action.reach_pose.target_pose
        cartesian_pose.x = 0.45072677731513977      # (meters)
        cartesian_pose.y = -0.38451656699180603          # (meters)
        cartesian_pose.z = 0.08602050691843033 + 0.2       # (meters)
        cartesian_pose.theta_x = 177.23646545410156 # (degrees)
        cartesian_pose.theta_y = 1.1521186828613281 # (degrees)
        cartesian_pose.theta_z = 93.01216888427734 # (degrees)

        e = threading.Event()
        notification_handle = base.OnNotificationActionTopic(
            check_for_end_or_abort(e),
            Base_pb2.NotificationOptions()
        )
        base.ExecuteAction(action)

        print("Waiting for movement to finish ...")
        finished = e.wait(20)
        base.Unsubscribe(notification_handle)

        if finished:
            print("Cartesian movement completed")
        else:
            print("Timeout on action notification wait")


def grasp(args):
    with utilities.DeviceConnection.createTcpConnection(args) as router:
        base = BaseClient(router)
        base_cyclic = BaseCyclicClient(router)
        control = ControlConfigClient(router)

        action = Base_pb2.Action()
        action.name = "Example Cartesian action movement"
        action.application_data = ""
        cartesian_pose = action.reach_pose.target_pose
        cartesian_pose.x = 0.45072677731513977      # (meters)
        cartesian_pose.y = -0.38451656699180603          # (meters)
        cartesian_pose.z = 0.08602050691843033       # (meters)
        cartesian_pose.theta_x = 177.23646545410156 # (degrees)
        cartesian_pose.theta_y = 1.1521186828613281 # (degrees)
        cartesian_pose.theta_z = 93.01216888427734 # (degrees)

        e = threading.Event()
        notification_handle = base.OnNotificationActionTopic(
            check_for_end_or_abort(e),
            Base_pb2.NotificationOptions()
        )
        base.ExecuteAction(action)

        print("Waiting for movement to finish ...")
        finished = e.wait(20)
        base.Unsubscribe(notification_handle)

        if finished:
            print("Cartesian movement completed")
        else:
            print("Timeout on action notification wait")

def drop(args):
    with utilities.DeviceConnection.createTcpConnection(args) as router:
        base = BaseClient(router)
        base_cyclic = BaseCyclicClient(router)
        control = ControlConfigClient(router)

        action = Base_pb2.Action()
        action.name = "Example Cartesian action movement"
        action.application_data = ""
        cartesian_pose = action.reach_pose.target_pose
        cartesian_pose.x = -0.231      # (meters)
        cartesian_pose.y = -0.371          # (meters)
        cartesian_pose.z = 0.302       # (meters)
        cartesian_pose.theta_x = 177.23646545410156 # (degrees)
        cartesian_pose.theta_y = 1.1521186828613281 # (degrees)
        cartesian_pose.theta_z = 93.01216888427734 # (degrees)

        e = threading.Event()
        notification_handle = base.OnNotificationActionTopic(
            check_for_end_or_abort(e),
            Base_pb2.NotificationOptions()
        )
        base.ExecuteAction(action)

        print("Waiting for movement to finish ...")
        finished = e.wait(20)
        base.Unsubscribe(notification_handle)

        if finished:
            print("Cartesian movement completed")
        else:
            print("Timeout on action notification wait")

if __name__ == "__main__":
    args = utilities.parseConnectionArguments()
    pre_grasp(args)
    grasp(args)
    gripper_close(args)
    pre_grasp(args)
    drop(args)