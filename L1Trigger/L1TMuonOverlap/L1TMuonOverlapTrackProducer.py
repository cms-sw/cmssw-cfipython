import FWCore.ParameterSet.Config as cms

def L1TMuonOverlapTrackProducer(*args, **kwargs):
  mod = cms.EDProducer('L1TMuonOverlapTrackProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
