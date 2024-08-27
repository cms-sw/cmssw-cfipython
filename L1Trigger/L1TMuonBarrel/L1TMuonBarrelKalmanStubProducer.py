import FWCore.ParameterSet.Config as cms

def L1TMuonBarrelKalmanStubProducer(**kwargs):
  mod = cms.EDProducer('L1TMuonBarrelKalmanStubProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
