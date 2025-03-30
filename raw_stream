from pylsl import StreamInlet, resolve_streams
import time

print("Looking for EEG streams...")

# Finds all active LSL streams.
streams = resolve_streams()

# Loops through each stream 's' in 'streams'
# if s.type() is EEG
# 'next' gets the first match.
eeg_stream = next(s for s in streams if s.type() == 'EEG')

# Connects the code to the EEG data stream.
inlet = StreamInlet(eeg_stream)


print("Streaming EEG data...")
# Loop outputting the milli volts
# of the four EEG channels.
# TODO: Determine which channels is which.
while True:
    sample, timestamp = inlet.pull_sample()

    ch0 = sample[0]
    ch1 = sample[1]
    ch2 = sample[2]
    ch3 = sample[3]

    # Outputs each channel's data, rounded to the
    # second decimal place.
    print(f"Stream 0: {ch0:.2f}| Stream 1: {ch1:.2f} "
          f"| Stream 2: {ch2:.2f} | Stream 3: {ch3:.2f}")
    # Displays a sample every 0.2 seconds.
    time.sleep(0.2)

