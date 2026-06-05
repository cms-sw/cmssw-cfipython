import FWCore.ParameterSet.Config as cms

def PatBasicAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PatBasicAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
