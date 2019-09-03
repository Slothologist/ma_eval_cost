import pickle

pipeline = 'pipeline1'

filename_to_utterance = {
    '01': 'hallo flobi',
    '02': 'mein name ist',
    '03': 'ja das stimmt',
    '04': 'nein das moechte ich nicht',
    '05': 'okay ist in ordnung',
    '06': 'gut das mache ich',
    '07': 'wo kommt denn der koch loeffel hin',
    '08': 'was muss ich machen',
    '09': 'ich brauche deine hilfe',
    '10': 'mach das licht in der kueche an',
    '11': 'beleuchtung bitte',
    '12': 'wo geht das licht an',
    '13': 'schick mir flobi in die kueche',
    '14': 'kann ich was zu trinken haben',
    '15': 'ist der geschirrspueler fertig',
    '16': 'flobi wo sind die glaeser',
    '17': 'wo sind die glaeser',
    '18': 'entspannungsmodus starten',
    '19': 'ich bin fertig damit',
    '20': 'okay',
    '21': 'ja',
    '22': 'nein',
    '23': 'auf wiedersehen',
    '24': 'tschuess'
}

utterance_to_filename = {filename_to_utterance[x] : x for x in filename_to_utterance}

amount_of_correct_recognitions = 0
amount_of_samples = 1723
max_time = 0.
min_time = 1000000.
chunkos = []

segmented = []
with open('saved_time/' + pipeline + '/p2_segmentations.txt', 'r') as file:
    segmented = file.readlines()

print('len segmented: ' + str(len(segmented)))

with open('saved_time/' + pipeline + '/p2.txt', 'r') as file:
    complete_file = file.read()

    # aquire starting time
    first_section, second_section = complete_file.split('\n\n\n\n')
    first_section = first_section.strip()
    starting_time = int(first_section.split(':')[1].strip())

    # chunk all responses together
    chunked = second_section.strip().split('\n\n')
    print('len chunked: ' + str(len(chunked)))
    for a in range(len(chunked)):
        chunk = chunked[a]
        segmenta = segmented[a]
        if 'none' in chunk:
            continue
        recording = chunk.split(':')[0].split(' of ')[1].split('\n')[0].strip()
        time = (int(chunk.split(':')[1].strip()) - starting_time) * 10e-10 + 0
        seg_time = (int(segmenta.split(':')[1].strip()) - starting_time) * 10e-10
        if not recording == 'null':
            if 'mein name ist' in recording:
                recording = 'mein name ist'
            chunkos.append((utterance_to_filename[recording], time, seg_time))

with open('./annotated_wav_file.pickle', 'r') as fileo:
    annots = pickle.load(fileo)

print('len chunkos: ' + str(len(chunkos)))

for a in range(min(len(chunkos), len(annots))):
    pass#print(annots[a], chunkos[a])

for a in range(min(len(chunkos), len(annots)), max(len(chunkos), len(annots))):
    pass#print(annots[a])

# match results
matches = []

for anno in annots:
    match = None
    for rec in chunkos:
        if anno[1] < rec[1] < anno[1] + 2 and rec[0] == anno[0]:
            match = rec
    if match:
        matches.append((anno[0], anno[1], match[1], match[2]))

timings = [x[2]-x[1] for x in matches]
seg_timings = [x[3]-x[1] for x in matches]

print(len(matches)/float(amount_of_samples))
print(sum(timings)/len(matches))
print(max(timings))
print(min(timings))

print('----------')

print(sum(seg_timings)/len(matches))
print(max(seg_timings))
print(min(seg_timings))