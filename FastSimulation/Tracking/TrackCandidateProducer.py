import FWCore.ParameterSet.Config as cms

def TrackCandidateProducer(**kwargs):
  mod = cms.EDProducer('TrackCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
