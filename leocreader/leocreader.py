from easyocr import Reader

LeOCReader = Reader(
    ["ko"],
    gpu=True,
    model_storage_directory="./user_network_dir",
    user_network_directory="./user_network_dir",
    recog_network="custom",
)
