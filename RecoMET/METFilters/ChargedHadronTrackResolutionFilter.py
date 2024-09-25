import FWCore.ParameterSet.Config as cms

def ChargedHadronTrackResolutionFilter(*args, **kwargs):
  mod = cms.EDFilter('ChargedHadronTrackResolutionFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
