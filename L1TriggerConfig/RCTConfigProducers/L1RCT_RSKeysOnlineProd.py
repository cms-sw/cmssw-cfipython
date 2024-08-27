import FWCore.ParameterSet.Config as cms

def L1RCT_RSKeysOnlineProd(**kwargs):
  mod = cms.ESProducer('L1RCT_RSKeysOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
