# Python Built-in Modules
import wave

# Third-Party Libraries
import torch


class MeldAudioPreprocessor:
    """
    Preprocessor class for the audio files, turning them into tensors,
    for better compatibility with TPU traininga without affecting negatively
    CPU-based training.
    """

    def __init__(self):
        """
        Creates a new instance of the MeldAudioPreprocessor class with the
        the `dtype_map` instantiated
        """
        self.dtype_map = {
            1: torch.int8,
            2: torch.int16,
            4: torch.int32,
        }

    def __call__(self, x: wave.Wave_read) -> torch.Tensor:
        """
        Preprocesses the audio by converting it to a tensor.

        :param x: The audio to be preprocessed
        :return: The preprocessed audio, no padding or truncation applied
        """
        data = x.readframes(x.getnframes())
        dtype = self.dtype_map[x.getsampwidth()]
        samples = torch.frombuffer(data, dtype=dtype).float()
        samples = samples.reshape(-1, x.getnchannels())
        return samples.flatten()
