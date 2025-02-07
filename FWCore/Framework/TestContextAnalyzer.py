import FWCore.ParameterSet.Config as cms

def TestContextAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TestContextAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
