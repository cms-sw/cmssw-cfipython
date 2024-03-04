import FWCore.ParameterSet.Config as cms

def SiPixelTemplateStoreESProducer(**kwargs):
  mod = cms.ESProducer('SiPixelTemplateStoreESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
