from sqlalchemy import Column, Integer, String
from .meta import Base

class Matakuliah(Base):
    __tablename__ = 'matakuliah'
    
    id = Column(Integer, primary_key=True)
    kode_mk = Column(String(20), nullable=False)
    nama_mk = Column(String(255), nullable=False)
    sks = Column(Integer, nullable=False)
    semester = Column(String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'kode_mk': self.kode_mk,
            'nama_mk': self.nama_mk,
            'sks': self.sks,
            'semester': self.semester,
        }
