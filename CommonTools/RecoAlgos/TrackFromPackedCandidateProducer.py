import FWCore.ParameterSet.Config as cms

def TrackFromPackedCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackFromPackedCandidateProducer',
    PFCandidates = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
