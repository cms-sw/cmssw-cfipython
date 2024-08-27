import FWCore.ParameterSet.Config as cms

def L1SubsystemKeysOnlineProd(**kwargs):
  mod = cms.ESProducer('L1SubsystemKeysOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
