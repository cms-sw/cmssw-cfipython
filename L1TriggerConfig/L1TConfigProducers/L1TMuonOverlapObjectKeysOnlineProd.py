import FWCore.ParameterSet.Config as cms

def L1TMuonOverlapObjectKeysOnlineProd(**kwargs):
  mod = cms.ESProducer('L1TMuonOverlapObjectKeysOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
