from audio_separator.separator import Separator

# Initialize the Separator with other configuration properties, below
separator = Separator()

# Load a model
#separator.load_model(model_filename='UVR-MDX-NET-Inst_HQ_3.onnx')
#separator.load_model(model_filename="model_bs_roformer_ep_317_sdr_12.9755.ckpt")
#separator.load_model(model_filename='UVR_MDXNET_KARA_2.onnx')
separator.load_model(model_filename="htdemucs_6s.yaml")


#file1 = "/Volumes/DATA3/media2/mp3/01 Kimi wa Melody.mp3"
#file2 = "/Volumes/DATA3/media2/mp3/04 - Lullaley.mp3"
#file3 = "/Volumes/DATA3/media2/mp3/Fourplay_07-Bali Run.mp3"
file4 = "/Volumes/DATA3/media2/mp3/maesa_piano.mp3"


def print_hi(name):
    # Separate multiple audio files without reloading the model
    output_file_paths_1 = separator.separate(file4)
    #output_file_paths_2 = separator.separate(file2)
    #output_file_paths_3 = separator.separate(file3)
    print(output_file_paths_1)


if __name__ == '__main__':
    print_hi('PyCharm')



