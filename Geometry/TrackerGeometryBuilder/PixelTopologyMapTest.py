import FWCore.ParameterSet.Config as cms

def PixelTopologyMapTest(**kwargs):
  mod = cms.EDAnalyzer('PixelTopologyMapTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
