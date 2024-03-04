import FWCore.ParameterSet.Config as cms

def LargeSiStripClusterEvents(**kwargs):
  mod = cms.EDFilter('LargeSiStripClusterEvents',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
