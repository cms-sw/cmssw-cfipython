import FWCore.ParameterSet.Config as cms

def ChargedHadronTrackResolutionFilter(**kwargs):
  mod = cms.EDFilter('ChargedHadronTrackResolutionFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
