import FWCore.ParameterSet.Config as cms

def AlignmentCSCOverlapSelectorModule(**kwargs):
  mod = cms.EDFilter('AlignmentCSCOverlapSelectorModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
