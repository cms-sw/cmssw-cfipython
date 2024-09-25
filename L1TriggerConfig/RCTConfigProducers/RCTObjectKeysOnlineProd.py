import FWCore.ParameterSet.Config as cms

def RCTObjectKeysOnlineProd(*args, **kwargs):
  mod = cms.ESProducer('RCTObjectKeysOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
