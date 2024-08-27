import FWCore.ParameterSet.Config as cms

def CandTrackPtIsolationProducer(**kwargs):
  mod = cms.EDProducer('CandTrackPtIsolationProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
