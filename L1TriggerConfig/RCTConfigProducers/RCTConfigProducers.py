import FWCore.ParameterSet.Config as cms

def RCTConfigProducers(**kwargs):
  mod = cms.ESProducer('RCTConfigProducers',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
