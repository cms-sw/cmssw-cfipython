import FWCore.ParameterSet.Config as cms

def LargestPtTrackSelector(**kwargs):
  mod = cms.EDFilter('LargestPtTrackSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
