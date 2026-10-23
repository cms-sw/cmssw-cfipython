import FWCore.ParameterSet.Config as cms

def ESTestAnalyzerJ(*args, **kwargs):
  mod = cms.EDAnalyzer('ESTestAnalyzerJ',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
