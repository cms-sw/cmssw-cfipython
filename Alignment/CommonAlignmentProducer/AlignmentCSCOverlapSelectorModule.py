import FWCore.ParameterSet.Config as cms

def AlignmentCSCOverlapSelectorModule(*args, **kwargs):
  mod = cms.EDFilter('AlignmentCSCOverlapSelectorModule',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
