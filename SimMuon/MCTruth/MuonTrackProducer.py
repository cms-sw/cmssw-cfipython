import FWCore.ParameterSet.Config as cms

def MuonTrackProducer(**kwargs):
  mod = cms.EDProducer('MuonTrackProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
