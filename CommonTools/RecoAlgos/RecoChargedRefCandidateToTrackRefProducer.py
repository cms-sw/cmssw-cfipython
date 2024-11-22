import FWCore.ParameterSet.Config as cms

def RecoChargedRefCandidateToTrackRefProducer(*args, **kwargs):
  mod = cms.EDProducer('RecoChargedRefCandidateToTrackRefProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
