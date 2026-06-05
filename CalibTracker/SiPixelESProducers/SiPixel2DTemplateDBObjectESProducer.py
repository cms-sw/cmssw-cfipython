import FWCore.ParameterSet.Config as cms

def SiPixel2DTemplateDBObjectESProducer(*args, **kwargs):
  mod = cms.ESProducer('SiPixel2DTemplateDBObjectESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
