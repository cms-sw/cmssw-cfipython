import FWCore.ParameterSet.Config as cms

def RCTObjectKeysOnlineProd(**kwargs):
  mod = cms.ESProducer('RCTObjectKeysOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
