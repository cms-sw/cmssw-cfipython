import FWCore.ParameterSet.Config as cms

def SiPixelGenErrorDBObjectESProducer(**kwargs):
  mod = cms.ESProducer('SiPixelGenErrorDBObjectESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
