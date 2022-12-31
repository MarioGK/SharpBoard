import time
import keyboardManager

#keyboard_handle_events_task = asyncio.create_task(keyboardManager.handle_events())

while True:
    start = time.monotonic_ns()
    #asyncio.gather(keyboard_handle_events_task)
    keyboardManager.handle_events()
    end = time.monotonic_ns()
    duration = end - start
    # Convert duration from nanoseconds to milliseconds
    duration_ms = duration / 1000000
    print("Time: " + str(duration_ms))
