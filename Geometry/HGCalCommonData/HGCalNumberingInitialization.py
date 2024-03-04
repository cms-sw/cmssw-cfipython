import FWCore.ParameterSet.Config as cms

def HGCalNumberingInitialization(**kwargs):
  mod = cms.ESProducer('HGCalNumberingInitialization',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
