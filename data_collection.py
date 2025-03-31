from signal_processing import bandpass_filter

# Used for streaming EEG data.
from pylsl import StreamInlet, resolve_streams
import time

# For visualising the data.
import matplotlib.pyplot as plt

# Plots the filtered and unfiltered data.
def plot_channel(ax, timestamps, raw_data, raw_label, filtered_data, filtered_label, title):
    ax.plot(timestamps, raw_data, label=raw_label)
    ax.plot(timestamps, filtered_data, label=filtered_label)
    ax.set_title(title)
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Amplitude (microvolts)")
    ax.legend()

print("Looking for EEG streams...")

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
# Loop outputting the microvolts
# of the four EEG channels.

count = 0

# Separate channel lists for storing sample and
# timestamp values.
tp9_raw = []
tp9_timestamp = []

tp10_raw = []
tp10_timestamp = []

af7_raw = []
af7_timestamp = []

af8_raw = []
af8_timestamp = []

while True:
    sample, timestamp = inlet.pull_sample()

    # Samples from the four EEG channels.
    tp9 = (sample[0])
    af7 = (sample[1])
    af8 = (sample[2])
    tp10 = (sample[3])

    # Outputs each channel's data, rounded to the
    # second decimal place.
    # print(f"TP9: {tp9:.2f}| AF7: {af7:.2f} "
    #       f"| AF8: {af8:.2f} | TP10: {tp10:.2f}")

    # Adds a delay to sample collection.
    time.sleep(0)

    # Appends the sample and timestamp to the
    # corresponding list.

    tp9_raw.append(sample[0])
    tp9_timestamp.append(timestamp)

    af7_raw.append(sample[1])
    af7_timestamp.append(timestamp)

    af8_raw.append(sample[2])
    af8_timestamp.append(timestamp)

    tp10_raw.append(sample[3])
    tp10_timestamp.append(timestamp)

    # For each increment in count 256 samples are collected.
    count += 1

    # 1024 samples over 4 seconds.
    if count == 256 * 10:
        break

# Filtering the channels using bandpass_filter.
tp9_filtered = bandpass_filter(tp9_raw)
tp10_filtered = bandpass_filter(tp10_raw)
af7_filtered = bandpass_filter(af7_raw)
af8_filtered = bandpass_filter(af8_raw)

# Creating a 2x2 grid of subplots.
figs, axs = plt.subplots(2, 2, figsize=(12, 8))

# Plots comparing the raw and filtered data
# from each channel.

# TP9 Plot
plot_channel(axs[0][0], tp9_timestamp, tp9_raw, "Raw TP9", tp9_filtered,
             "Filtered  TP9", "Raw TP9 Data vs. Filtered TP9 Data")
# TP10 Plot
plot_channel(axs[0][1], tp10_timestamp, tp10_raw, "Raw TP10", tp10_filtered,
             "Filtered TP10", "Raw TP10 Data vs. Filtered TP10 Data")
# AF7 Plot
plot_channel(axs[1][0], af7_timestamp, af7_raw, "Raw AF7", af7_filtered,
             "Filtered AF7", "Raw AF7 Data vs. Filtered AF7 Data")
# AF8 Plot
plot_channel(axs[1][1], af8_timestamp, af8_raw, "Raw AF8", af8_filtered,
             "Filtered AF8", "Raw AF8 Data vs. Filtered AF8 Data")

plt.show()


