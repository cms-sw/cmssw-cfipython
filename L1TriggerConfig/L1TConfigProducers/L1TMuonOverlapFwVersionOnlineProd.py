import FWCore.ParameterSet.Config as cms

def L1TMuonOverlapFwVersionOnlineProd(*args, **kwargs):
  mod = cms.ESProducer('L1TMuonOverlapFwVersionOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
