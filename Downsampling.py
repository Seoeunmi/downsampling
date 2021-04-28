import librosa
import soundfile as sf
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Issue: Creating directory. ' +  directory)

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
    resample = librosa.resample(y, sr, resample_sr)
    print("\r original wav sr: {}, original wav shape: {}, resample wav sr: {}, resmaple shape: {}".format(origin_sr, y.shape, resample_sr, resample.shape))
    createFolder(save_path)
    sf.write(save_path + '/{}'.format(input_wav[-12:]), resample, resample_sr, format='WAV', endian='LITTLE')

save_path = './data/downsample'
dir_name = '/home/eunmi/PycharmProjects/downsampling/data/test'
file_name = read_path_list(dir_name, extention='wav')
for i in range(len(file_name)):
    down_sample(file_name[i], 16000, 4000, save_path)
