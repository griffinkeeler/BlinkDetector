# Used for connecting to the Muse 2 via bluetooth.
import muselsl
from muselsl import stream
import multiprocessing

# Used for streaming EEG data.
from pylsl import StreamInlet, resolve_streams
import time

# For visualising the data.
import matplotlib.pyplot as plt

print("Looking for EEG streams...")

# Connects to the Muse 2 if found.
p = multiprocessing.Process(target=stream)
p.start()

# Gives the stream time to initialise.
time.sleep(5)
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

count = 0

# Separate channel lists for storing sample and
# timestamp values.
tp9_sample = []
tp9_timestamp = []

tp10_sample = []
tp10_timestamp = []

af7_sample = []
af7_timestamp = []

af8_sample = []
af8_timestamp = []

while True:
    sample, timestamp = inlet.pull_sample()

    tp9 = sample[0]
    af7 = sample[1]
    af8 = sample[2]
    tp10 = sample[3]

    # Outputs each channel's data, rounded to the
    # second decimal place.
    print(f"TP9: {tp9:.2f}| AF7: {af7:.2f} "
          f"| AF8: {af8:.2f} | TP10: {tp10:.2f}")

    # Collects a sample every 0.5 seconds.
    time.sleep(0.01)

    # Appends the sample and timestamp to the
    # corresponding list.

    tp9_sample.append(sample[0])
    tp9_timestamp.append(timestamp)

    af7_sample.append(sample[1])
    af7_timestamp.append(timestamp)

    af8_sample.append(sample[2])
    af8_timestamp.append(timestamp)

    tp10_sample.append(sample[3])
    tp10_timestamp.append(timestamp)

    count += 1
    if count == 100:
        break

# Plot showing the voltage (mV) reading
# of each channel over time.
tp9_plot = plt.plot(tp9_timestamp, tp9_sample)
tp10_plot = plt.plot(tp10_timestamp, tp10_sample)
af7_plot = plt.plot(af7_timestamp, af7_sample)
af8_plot = plt.plot(af8_timestamp, af8_sample)
plt.show()



