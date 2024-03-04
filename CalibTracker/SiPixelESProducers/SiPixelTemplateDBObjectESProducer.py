import FWCore.ParameterSet.Config as cms

def SiPixelTemplateDBObjectESProducer(**kwargs):
  mod = cms.ESProducer('SiPixelTemplateDBObjectESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
