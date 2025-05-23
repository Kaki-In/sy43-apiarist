import database as _database
import database_layering.facades as _database_layering_facades

class NoobleActivitySaveFile(_database_layering_facades.DatabaseElementFacade[int]):
    def get_id(self) -> int:
        return self.get_element().get_configuration().get_id()
    
    def get_type(self) -> str:
        return self.get_element().get("type")[0]
    
    def get_content(self) -> bytes:
        return self.get_element().get("content")[0]
    
    def get_section(self) -> int:
        return int(self.get_element().get("section")[0])
    
    def set_content(self, content: bytes) -> None:
        self.get_element().set(
            content = _database.SQLBlob(content)
        )

