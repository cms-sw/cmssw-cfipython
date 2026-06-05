import FWCore.ParameterSet.Config as cms

def PixelTopologyMapTest(*args, **kwargs):
  mod = cms.EDAnalyzer('PixelTopologyMapTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
