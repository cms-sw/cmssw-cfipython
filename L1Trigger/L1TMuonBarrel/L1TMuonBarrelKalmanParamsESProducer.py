import FWCore.ParameterSet.Config as cms

def L1TMuonBarrelKalmanParamsESProducer(**kwargs):
  mod = cms.ESProducer('L1TMuonBarrelKalmanParamsESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
