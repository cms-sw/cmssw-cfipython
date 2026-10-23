import FWCore.ParameterSet.Config as cms

def LumiTestReadAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('LumiTestReadAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
