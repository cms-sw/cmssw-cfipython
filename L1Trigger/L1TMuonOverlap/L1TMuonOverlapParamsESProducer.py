import FWCore.ParameterSet.Config as cms

def L1TMuonOverlapParamsESProducer(**kwargs):
  mod = cms.ESProducer('L1TMuonOverlapParamsESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
