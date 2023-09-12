from collections import namedtuple


DataIngestionArtifact = namedtuple("DataIngestionArtifact",
                                   ["train_file_path","Test_file_path","isingested","message"])
