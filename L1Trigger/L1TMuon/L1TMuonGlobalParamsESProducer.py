import FWCore.ParameterSet.Config as cms

def L1TMuonGlobalParamsESProducer(**kwargs):
  mod = cms.ESProducer('L1TMuonGlobalParamsESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
