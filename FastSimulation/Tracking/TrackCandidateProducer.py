import FWCore.ParameterSet.Config as cms

def TrackCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
