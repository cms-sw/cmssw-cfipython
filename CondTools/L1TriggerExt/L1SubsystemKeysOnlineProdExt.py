import FWCore.ParameterSet.Config as cms

def L1SubsystemKeysOnlineProdExt(*args, **kwargs):
  mod = cms.ESProducer('L1SubsystemKeysOnlineProdExt',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
