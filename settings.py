class Settings:

    def __init__(self):
        self.raw_data_path = "./data/raw/"
        self.processed_data_path = "./data/processed/"

        self.raw_data_filename = "bases de datos SM.xlsx"

    def get_raw_data_path(self):
        return self.raw_data_path + self.raw_data_filename