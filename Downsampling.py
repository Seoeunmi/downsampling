import librosa
import soundfile as sf
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Issue: Creating directory. ' + directory)

def load_path():
    path = os.path.join(os.path.dirname(__file__))
    if path == "":
        path = "."
    return path

def read_path_list(dirname, extention=""):
    try:
        return_list = []
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                return_list.extend(read_path_list(full_filename, extention))
            else:
                ext = os.path.splitext(full_filename)[-1][1:]
                if extention == "" or ext == extention:
                    return_list.append(full_filename)
        return_list.sort()
        return return_list
    except PermissionError:
        pass

def down_sample(input_wav, origin_sr, resample_sr, save_path):
    y, sr = librosa.load(input_wav, sr=origin_sr)
    if sr != origin_sr:
        raise Exception("ERROR: Sampling rate isn't %d".format(origin_sr))

    resample = librosa.resample(y, sr, resample_sr)
    print("\r original wav sr: {}, original wav shape: {}, resample wav sr: {}, resmaple shape: {}".format(origin_sr, y.shape, resample_sr, resample.shape))
    sf.write(save_path + '/' + os.path.basename(file_name[i]), resample, resample_sr, format='WAV', endian='LITTLE')


dir_name = '/home/eunmi/PycharmProjects/downsampling/data/'
file_name = read_path_list(dir_name, extention='wav')

for i in range(len(file_name)):
    save_path = load_path() + '/generate_data' + os.path.dirname(file_name[i].replace(dir_name, "").replace(os.path.basename(file_name[i]), ""))
    createFolder(save_path)
    down_sample(file_name[i], 16000, 8000, save_path)
