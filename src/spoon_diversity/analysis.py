from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class TrialMetrics:
	operations_per_second: Optional[float]
	errors_per_operation: Optional[float]
	switch_overhead_fraction: Optional[float]


def compute_operations_per_second(num_operations: Optional[int], time_seconds: Optional[float]) -> Optional[float]:
	if num_operations is None or time_seconds is None:
		return None
	if time_seconds <= 0:
		return None
	return float(num_operations) / float(time_seconds)


def compute_errors_per_operation(error_rate_percent: Optional[float], num_operations: Optional[int]) -> Optional[float]:
	if error_rate_percent is None or num_operations is None:
		return None
	if num_operations <= 0:
		return None
	# Interpret error_rate_percent as percentage of operations that were errors
	return (float(error_rate_percent) / 100.0)


def compute_switch_overhead_fraction(switch_time_seconds: Optional[float], time_seconds: Optional[float]) -> Optional[float]:
	if switch_time_seconds is None or time_seconds is None:
		return None
	if time_seconds <= 0:
		return None
	return float(switch_time_seconds) / float(time_seconds)


def compute_trial_metrics(
	num_operations: Optional[int],
	time_seconds: Optional[float],
	error_rate_percent: Optional[float],
	switch_time_seconds: Optional[float],
) -> TrialMetrics:
	return TrialMetrics(
		operations_per_second=compute_operations_per_second(num_operations, time_seconds),
		errors_per_operation=compute_errors_per_operation(error_rate_percent, num_operations),
		switch_overhead_fraction=compute_switch_overhead_fraction(switch_time_seconds, time_seconds),
	)

