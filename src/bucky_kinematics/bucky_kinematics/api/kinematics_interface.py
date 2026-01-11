"""High-level API for inverse kinematics."""

from typing import Optional
import numpy as np


class KinematicsInterface:
    """
    Main user-facing API for inverse kinematics.

    Usage:
        ik = KinematicsInterface.from_xacro("robot.urdf.xacro")
        solution = ik.solve_ik(target_pose, current_joints)
    """

    @classmethod
    def from_xacro(cls, xacro_path: str, **kwargs):
        """Initialize from XACRO file (auto-detects configuration)."""
        raise NotImplementedError("XACRO initialization not yet implemented")

    def solve_ik(
        self,
        target_pose: np.ndarray,
        current_joints: Optional[np.ndarray] = None,
        **kwargs
    ):
        """
        Solve inverse kinematics for target pose.

        Args:
            target_pose: 4x4 homogeneous transformation matrix
            current_joints: Current joint configuration (for solution selection)

        Returns:
            Best IK solution, or None if unreachable
        """
        raise NotImplementedError("IK solving not yet implemented")
