import FWCore.ParameterSet.Config as cms

def TestAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TestAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
