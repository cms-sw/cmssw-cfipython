import FWCore.ParameterSet.Config as cms

def BySiPixelClusterMultiplicityEventFilter(*args, **kwargs):
  mod = cms.EDFilter('BySiPixelClusterMultiplicityEventFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
