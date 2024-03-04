import FWCore.ParameterSet.Config as cms

def SiPixel2DTemplateDBObjectESProducer(**kwargs):
  mod = cms.ESProducer('SiPixel2DTemplateDBObjectESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
