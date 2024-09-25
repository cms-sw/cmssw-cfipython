import FWCore.ParameterSet.Config as cms

def L1TMuonBarrelKalmanTrackProducer(*args, **kwargs):
  mod = cms.EDProducer('L1TMuonBarrelKalmanTrackProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
