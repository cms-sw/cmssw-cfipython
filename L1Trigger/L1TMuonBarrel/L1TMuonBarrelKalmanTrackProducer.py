import FWCore.ParameterSet.Config as cms

def L1TMuonBarrelKalmanTrackProducer(**kwargs):
  mod = cms.EDProducer('L1TMuonBarrelKalmanTrackProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
