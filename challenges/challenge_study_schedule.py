def study_schedule(permanence_period, target_time):
    count = 0
    if target_time is None:
        return None
    for enter_time, exit_time in permanence_period:
        if not isinstance(enter_time, int) or not isinstance(exit_time, int):
            return None
        if target_time >= enter_time and target_time <= exit_time:
            count += 1
    return count

    raise NotImplementedError
