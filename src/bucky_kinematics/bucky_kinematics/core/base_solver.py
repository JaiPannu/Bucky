"""Base classes for IK solvers."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional
import numpy as np


@dataclass
class IKSolution:
    """Represents a single IK solution."""
    joint_angles: np.ndarray
    configuration: str
    reachable: bool
    error: float = 0.0


@dataclass
class IKRequest:
    """Request for inverse kinematics computation."""
    target_pose: np.ndarray
    current_joints: Optional[np.ndarray] = None
    constraints: Optional[dict] = None


class BaseSolver(ABC):
    """Abstract base class for all IK solvers."""

    def __init__(self, dh_params, joint_limits):
        self.dh_params = dh_params
        self.joint_limits = joint_limits

    @abstractmethod
    def solve(self, request: IKRequest) -> List[IKSolution]:
        """Solve inverse kinematics and return all valid solutions."""
        pass

    @abstractmethod
    def forward_kinematics(self, joint_angles: np.ndarray) -> np.ndarray:
        """Compute forward kinematics for verification."""
        pass
