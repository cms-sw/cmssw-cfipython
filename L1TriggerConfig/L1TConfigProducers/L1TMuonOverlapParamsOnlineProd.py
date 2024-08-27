import FWCore.ParameterSet.Config as cms

def L1TMuonOverlapParamsOnlineProd(**kwargs):
  mod = cms.ESProducer('L1TMuonOverlapParamsOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
