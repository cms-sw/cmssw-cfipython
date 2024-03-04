import FWCore.ParameterSet.Config as cms

def PixelClusterShapeExtractor(**kwargs):
  mod = cms.EDAnalyzer('PixelClusterShapeExtractor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
