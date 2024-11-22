import FWCore.ParameterSet.Config as cms

def TrackViewCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackViewCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
