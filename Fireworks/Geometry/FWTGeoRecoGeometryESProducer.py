import FWCore.ParameterSet.Config as cms

def FWTGeoRecoGeometryESProducer(**kwargs):
  mod = cms.ESProducer('FWTGeoRecoGeometryESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
