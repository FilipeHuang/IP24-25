def nested_exceptions(一):
    if isinstance(一,tuple): return tuple(nested_exceptions(二) for 二 in 一)
    try:
        一()
        return False
    except Exception: return True