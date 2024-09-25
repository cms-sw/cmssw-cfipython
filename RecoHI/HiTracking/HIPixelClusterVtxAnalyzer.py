import FWCore.ParameterSet.Config as cms

def HIPixelClusterVtxAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HIPixelClusterVtxAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
