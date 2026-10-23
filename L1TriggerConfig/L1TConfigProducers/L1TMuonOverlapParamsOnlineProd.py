import FWCore.ParameterSet.Config as cms

def L1TMuonOverlapParamsOnlineProd(*args, **kwargs):
  mod = cms.ESProducer('L1TMuonOverlapParamsOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
