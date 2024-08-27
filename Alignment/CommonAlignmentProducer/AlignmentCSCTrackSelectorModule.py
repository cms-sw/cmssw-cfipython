import FWCore.ParameterSet.Config as cms

def AlignmentCSCTrackSelectorModule(**kwargs):
  mod = cms.EDFilter('AlignmentCSCTrackSelectorModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
