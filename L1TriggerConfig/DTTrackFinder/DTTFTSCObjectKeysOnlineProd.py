import FWCore.ParameterSet.Config as cms

def DTTFTSCObjectKeysOnlineProd(*args, **kwargs):
  mod = cms.ESProducer('DTTFTSCObjectKeysOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
