import FWCore.ParameterSet.Config as cms

def L1TMuonOverlapPhase2TrackProducer(**kwargs):
  mod = cms.EDProducer('L1TMuonOverlapPhase2TrackProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
