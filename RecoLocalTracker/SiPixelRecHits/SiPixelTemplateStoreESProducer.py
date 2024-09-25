import FWCore.ParameterSet.Config as cms

def SiPixelTemplateStoreESProducer(*args, **kwargs):
  mod = cms.ESProducer('SiPixelTemplateStoreESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
