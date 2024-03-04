import FWCore.ParameterSet.Config as cms

def RecoChargedRefCandidateToTrackRefProducer(**kwargs):
  mod = cms.EDProducer('RecoChargedRefCandidateToTrackRefProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
