import FWCore.ParameterSet.Config as cms

def TrackFromPackedCandidateProducer(**kwargs):
  mod = cms.EDProducer('TrackFromPackedCandidateProducer',
    PFCandidates = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
