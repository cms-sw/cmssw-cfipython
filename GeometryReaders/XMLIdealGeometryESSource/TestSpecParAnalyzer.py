import FWCore.ParameterSet.Config as cms

def TestSpecParAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TestSpecParAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
