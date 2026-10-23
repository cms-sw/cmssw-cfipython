import FWCore.ParameterSet.Config as cms

def PixelClusterShapeExtractor(*args, **kwargs):
  mod = cms.EDAnalyzer('PixelClusterShapeExtractor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
