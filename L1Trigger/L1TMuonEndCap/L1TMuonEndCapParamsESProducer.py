import FWCore.ParameterSet.Config as cms

def L1TMuonEndCapParamsESProducer(**kwargs):
  mod = cms.ESProducer('L1TMuonEndCapParamsESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
