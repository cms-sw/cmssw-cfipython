import FWCore.ParameterSet.Config as cms

def AlignmentMuonSelectorModule(*args, **kwargs):
  mod = cms.EDFilter('AlignmentMuonSelectorModule',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
