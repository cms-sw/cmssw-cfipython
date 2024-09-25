import FWCore.ParameterSet.Config as cms

def InputAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('InputAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
