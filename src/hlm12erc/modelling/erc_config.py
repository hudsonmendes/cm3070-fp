# Local Folders
from .erc_feedforward import ERCFeedForwardActivation


class ERCTextEmbeddingType:
    GLOVE = "glove"


class ERCVisualEmbeddingType:
    RESNET_50 = "resnet50"


class ERCAudioEmbeddingType:
    WAVEFORM = "waveform"


class ERCFusionTechnique:
    STACKED = "stacked"


class ERCLossFunctions:
    CATEGORICAL_CROSS_ENTROPY = "categorical_cross_entropy"


class ERCConfig:
    """
    ERCConfig is a class that defines the configuration for ERC model.
    It is used to instantiate an ERC model according to the specified arguments,
    defining the model architecture.

    The classifier's objective is collapse highly-dimensional representations
    found in the audio-visual + textual raw data into a probability distribution
    ranging across the different emotion labels. These emotions are
    - anger,
    - disgust,
    - fear,
    - joy,
    - neutral
    - sadness
    - surprise
    """

    modules_text_encoder: str = ERCTextEmbeddingType.GLOVE
    modules_visual_encoder: str = ERCVisualEmbeddingType.RESNET_50
    modules_audio_encoder: str = ERCAudioEmbeddingType.WAVEFORM
    modules_fusion: str = ERCFusionTechnique.STACKED

    text_hidden_size: int = 300

    audio_in_features: int = 1
    audio_hidden_size: int = 64
    audio_num_layers: int = 3
    audio_dropout: float = 0.1
    audio_activation: str = ERCFeedForwardActivation.RELU

    feedforward_hidden_size: int = 768
    feedforward_num_layers: int = 3
    feedforward_dropout: float = 0.1
    feedforward_activation: str = ERCFeedForwardActivation.RELU

    classifier_n_classes: int = 7
    classifier_loss_fn: str = ERCLossFunctions.CATEGORICAL_CROSS_ENTROPY
