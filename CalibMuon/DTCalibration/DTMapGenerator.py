import FWCore.ParameterSet.Config as cms

def DTMapGenerator(*args, **kwargs):
  mod = cms.EDAnalyzer('DTMapGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
