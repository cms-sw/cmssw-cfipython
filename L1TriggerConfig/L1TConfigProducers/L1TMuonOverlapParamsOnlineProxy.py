import FWCore.ParameterSet.Config as cms

def L1TMuonOverlapParamsOnlineProxy(**kwargs):
  mod = cms.ESProducer('L1TMuonOverlapParamsOnlineProxy',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
