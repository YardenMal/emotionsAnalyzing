import pickle
import librosa
import warnings

from matplotlib import pyplot as plt

warnings.filterwarnings('ignore')
from utils import extract_feature
from pydub import AudioSegment
from pydub.utils import make_chunks

class emotion_model(object):
    def __init__(self):
        self.model = pickle.load(open("GB_classifier.model", "rb"))

    def predict(self, filename):
        # extract features and reshape it
        features = extract_feature(filename, mfcc=True, chroma=True, mel=True).reshape(1, -1)
        # predict
        result = self.model.predict(features)[0]
        # show the result !
        print(filename, result[0])
        return result
def emo_chart (speaker_file):
    myaudio = AudioSegment.from_file(speaker_file, "wav")
    len = librosa.get_duration(filename=speaker_file)
    chunk_length_ms = 10000 # pydub calculates in millisec
    chunks = make_chunks(myaudio,chunk_length_ms) #Make chunks of one sec
    emotions = []
    for i, chunk in enumerate(chunks):
        chunk_name = "{0}.wav".format(i)
        chunk.export(chunk_name, format="wav")
        emotions.append(emotion_model().predict(
            chunk_name ))
    # return emotions
    n = 0
    h = 0
    s = 0
    a = 0
    f = 0
    emo_num = 0
    emo_dict = {
        "neutral": n,
        "happy": h,
        "sad": s,
        "angry": a,
        "fearful": f,
    }
    for i in emotions:
        if i == 'neutral':
            emo_dict['neutral'] += 1
            emo_num += 1
        if i == 'happy':
            emo_dict['happy'] += 1
            emo_num += 1
        if i == 'sad':
            emo_dict['sad'] += 1
            emo_num += 1
        if i == 'angry':
            emo_dict['angry'] += 1
            emo_num += 1
        if i == 'fearful':
            emo_dict['fearful'] += 1
            emo_num += 1
    dict ={
        "neutral": float("{:.1f}".format(((emo_dict['neutral']) / emo_num)*100)),
        "happy": float("{:.1f}".format(((emo_dict['happy']) / emo_num)*100)),
        "sad": float("{:.1f}".format(((emo_dict['sad']) / emo_num)*100)),
        "angry": float("{:.1f}".format(((emo_dict['angry']) / emo_num)*100)),
        "fearful": float("{:.1f}".format(((emo_dict['fearful']) / emo_num)*100)),
    }
    # Get the Keys and store them in a list
    labels = [*dict]
    # Get the Values and store them in a list
    values = [ list for key, list in dict.items()]

    for i in values:
        if i == '0.0%':
            idx= values.index(i)
            values.remove(i)
            labels.remove(labels[idx])

    plt.pie(values, labels=labels, startangle=90, autopct='%1.1f%%')
    plt.legend(loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

# print(emo_chart("1DmNV9C1hbY.wav"))

