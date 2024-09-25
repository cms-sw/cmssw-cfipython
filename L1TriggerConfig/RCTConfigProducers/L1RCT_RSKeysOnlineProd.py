import FWCore.ParameterSet.Config as cms

def L1RCT_RSKeysOnlineProd(*args, **kwargs):
  mod = cms.ESProducer('L1RCT_RSKeysOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
