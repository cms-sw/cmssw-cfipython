import FWCore.ParameterSet.Config as cms

def AlignmentSeedSelectorModule(**kwargs):
  mod = cms.EDFilter('AlignmentSeedSelectorModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
