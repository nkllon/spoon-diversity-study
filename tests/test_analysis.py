from __future__ import annotations

from spoon_diversity.analysis import (
	compute_operations_per_second,
	compute_errors_per_operation,
	compute_switch_overhead_fraction,
	compute_trial_metrics,
)


def test_metrics_ops_per_second():
	assert compute_operations_per_second(10, 5.0) == 2.0
	assert compute_operations_per_second(0, 5.0) == 0.0
	assert compute_operations_per_second(10, 0.0) is None
	assert compute_operations_per_second(None, 5.0) is None


def test_metrics_errors_per_op():
	assert compute_errors_per_operation(10.0, 20) == 0.1
	assert compute_errors_per_operation(0.0, 10) == 0.0
	assert compute_errors_per_operation(10.0, 0) is None
	assert compute_errors_per_operation(None, 10) is None


def test_metrics_switch_overhead():
	assert compute_switch_overhead_fraction(2.0, 10.0) == 0.2
	assert compute_switch_overhead_fraction(0.0, 10.0) == 0.0
	assert compute_switch_overhead_fraction(1.0, 0.0) is None


def test_compute_trial_metrics():
	m = compute_trial_metrics(10, 5.0, 10.0, 2.0)
	assert m.operations_per_second == 2.0
	assert m.errors_per_operation == 0.1
	assert m.switch_overhead_fraction == 0.4

