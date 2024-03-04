import FWCore.ParameterSet.Config as cms

def LargeSiPixelClusterEvents(**kwargs):
  mod = cms.EDFilter('LargeSiPixelClusterEvents',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
