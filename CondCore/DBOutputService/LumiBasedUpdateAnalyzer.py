import FWCore.ParameterSet.Config as cms

def LumiBasedUpdateAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('LumiBasedUpdateAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
