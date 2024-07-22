import FWCore.ParameterSet.Config as cms

def L1MuGMTRSKeysOnlineProd(**kwargs):
  mod = cms.ESProducer('L1MuGMTRSKeysOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod