total_inference_time = 4745.188561677933  # Your total inference time in seconds

# Convert seconds to hour:minute:second
hours, remainder = divmod(total_inference_time, 3600)
minutes, seconds = divmod(remainder, 60)

# Format and print the time
formatted_time = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
print(f"Eval: Total inference time: {formatted_time}")