import FWCore.ParameterSet.Config as cms

def SiPixelTemplateDBObjectESProducer(*args, **kwargs):
  mod = cms.ESProducer('SiPixelTemplateDBObjectESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
