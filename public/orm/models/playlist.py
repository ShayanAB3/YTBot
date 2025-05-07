from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship

from public.orm.base import Base

class Playlist(Base):
    __tablename__ = 'playlists'
    __allow_unmapped__ = True

    id = Column(BigInteger,primary_key=True)
    name = Column(String,nullable=False)
    author_id = Column(BigInteger,nullable=False)
    server_id = Column(BigInteger,nullable=False)

    # **Generated column**
    # SELECT JSON_ARRAYAGG(name) AS names_json, author_id, server_id FROM playlists GROUP BY author_id, server_id;
    names_json:str

    
    # Relation Ship
    tracks = relationship("Track", back_populates="playlist")
