import FWCore.ParameterSet.Config as cms

def TrackViewCandidateProducer(**kwargs):
  mod = cms.EDProducer('TrackViewCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
