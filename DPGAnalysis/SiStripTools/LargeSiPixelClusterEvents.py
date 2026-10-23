import FWCore.ParameterSet.Config as cms

def LargeSiPixelClusterEvents(*args, **kwargs):
  mod = cms.EDFilter('LargeSiPixelClusterEvents',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
