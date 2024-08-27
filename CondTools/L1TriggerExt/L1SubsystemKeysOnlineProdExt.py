import FWCore.ParameterSet.Config as cms

def L1SubsystemKeysOnlineProdExt(**kwargs):
  mod = cms.ESProducer('L1SubsystemKeysOnlineProdExt',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
