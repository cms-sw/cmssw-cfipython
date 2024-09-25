import FWCore.ParameterSet.Config as cms

def L1TMuonOverlapPhase1TrackProducer(*args, **kwargs):
  mod = cms.EDProducer('L1TMuonOverlapPhase1TrackProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
