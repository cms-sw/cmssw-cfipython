import FWCore.ParameterSet.Config as cms

def L1TMuonEndCapTrackProducer(**kwargs):
  mod = cms.EDProducer('L1TMuonEndCapTrackProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
