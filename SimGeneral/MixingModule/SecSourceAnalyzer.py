import FWCore.ParameterSet.Config as cms

def SecSourceAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('SecSourceAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
