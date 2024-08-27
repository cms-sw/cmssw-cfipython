import FWCore.ParameterSet.Config as cms

def L1MuGMTParametersKeysOnlineProd(**kwargs):
  mod = cms.ESProducer('L1MuGMTParametersKeysOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
