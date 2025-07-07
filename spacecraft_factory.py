class SpacecraftFactory:
    @staticmethod
    def create_spacecraft(spacecraft_type, *args, **kwargs):
        if spacecraft_type == "Fighter":
            return Fighter(*args, **kwargs)
        