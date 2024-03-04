import FWCore.ParameterSet.Config as cms

def AlignmentMuonSelectorModule(**kwargs):
  mod = cms.EDFilter('AlignmentMuonSelectorModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
