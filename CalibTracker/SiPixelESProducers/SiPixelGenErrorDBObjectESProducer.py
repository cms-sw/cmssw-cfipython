import FWCore.ParameterSet.Config as cms

def SiPixelGenErrorDBObjectESProducer(*args, **kwargs):
  mod = cms.ESProducer('SiPixelGenErrorDBObjectESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
