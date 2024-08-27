import FWCore.ParameterSet.Config as cms

def L1TMuonOverlapPhase1TrackProducer(**kwargs):
  mod = cms.EDProducer('L1TMuonOverlapPhase1TrackProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
