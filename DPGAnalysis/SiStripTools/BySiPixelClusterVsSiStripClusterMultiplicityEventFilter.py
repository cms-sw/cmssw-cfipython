import FWCore.ParameterSet.Config as cms

def BySiPixelClusterVsSiStripClusterMultiplicityEventFilter(*args, **kwargs):
  mod = cms.EDFilter('BySiPixelClusterVsSiStripClusterMultiplicityEventFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
