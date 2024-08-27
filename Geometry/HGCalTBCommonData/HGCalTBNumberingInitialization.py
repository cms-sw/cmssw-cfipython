import FWCore.ParameterSet.Config as cms

def HGCalTBNumberingInitialization(**kwargs):
  mod = cms.ESProducer('HGCalTBNumberingInitialization',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
