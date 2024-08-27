import FWCore.ParameterSet.Config as cms

def HIPixelClusterVtxAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HIPixelClusterVtxAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
