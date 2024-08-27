import FWCore.ParameterSet.Config as cms

def DTTFTSCObjectKeysOnlineProd(**kwargs):
  mod = cms.ESProducer('DTTFTSCObjectKeysOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
