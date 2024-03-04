import FWCore.ParameterSet.Config as cms

def AlignmentTrackSelectorModule(**kwargs):
  mod = cms.EDFilter('AlignmentTrackSelectorModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
