from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship

from public.orm.base import Base

class Track(Base):
    __tablename__ = "tracks"
    id = Column(BigInteger,primary_key=True)
    user_id = Column(BigInteger, nullable=False)
    server_id = Column(BigInteger,nullable=False)
    playlist_id = Column(BigInteger, ForeignKey("playlists.id"))

    title = Column(String,nullable=False)
    channel = Column(String,nullable=False)
    thumbnail = Column(String,nullable=False)
    webpage_url = Column(String,nullable=False)

    # RelationShip
    playlist = relationship("Playlist",back_populates="tracks")