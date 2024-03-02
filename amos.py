def convert_time(seconds):
  """Converts seconds to weeks, days, hours, minutes and seconds."""
  weeks = seconds // (7 * 24 * 60 * 60)
  remaining_seconds = seconds % (7 * 24 * 60 * 60)

  days = remaining_seconds // (24 * 60 * 60)
  remaining_seconds %= (24 * 60 * 60)

  hours = remaining_seconds // (60 * 60)
  remaining_seconds %= (60 * 60)

  minutes = remaining_seconds // 60
  seconds = remaining_seconds % 60

  return weeks, days, hours, minutes, seconds

# Get input from the user
user_input = int(input("Enter a number of seconds: "))

# Convert seconds and print the results
weeks, days, hours, minutes, seconds = convert_time(user_input)

print(f"{user_input} seconds is equal to:")
print(f"{weeks} weeks, {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")
