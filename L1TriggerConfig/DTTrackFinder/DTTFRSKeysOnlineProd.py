import FWCore.ParameterSet.Config as cms

def DTTFRSKeysOnlineProd(**kwargs):
  mod = cms.ESProducer('DTTFRSKeysOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
