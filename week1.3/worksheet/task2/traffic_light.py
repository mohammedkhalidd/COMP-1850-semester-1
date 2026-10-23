"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Mohammed Khalid Ibrahim
"""
states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())

state_order = ["red", "red_amber", "green", "amber"]
state_index = 0
time_in_state = 0

state = state_order[state_index]
print(f"Time {systime:03d} State {state}")

while systime < maxtime:
    systime += 1
    time_in_state += 1

    if time_in_state == states[state]:
        state_index = (state_index + 1) % len(state_order)
        state = state_order[state_index]
        time_in_state = 0

    print(f"Time {systime:03d} State {state}")