import FWCore.ParameterSet.Config as cms

def LargeSiStripClusterEvents(*args, **kwargs):
  mod = cms.EDFilter('LargeSiStripClusterEvents',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
