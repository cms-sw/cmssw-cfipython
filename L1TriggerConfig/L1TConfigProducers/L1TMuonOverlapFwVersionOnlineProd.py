import FWCore.ParameterSet.Config as cms

def L1TMuonOverlapFwVersionOnlineProd(**kwargs):
  mod = cms.ESProducer('L1TMuonOverlapFwVersionOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
