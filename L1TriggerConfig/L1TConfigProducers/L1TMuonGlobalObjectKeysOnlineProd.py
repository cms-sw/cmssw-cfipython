import FWCore.ParameterSet.Config as cms

def L1TMuonGlobalObjectKeysOnlineProd(**kwargs):
  mod = cms.ESProducer('L1TMuonGlobalObjectKeysOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
