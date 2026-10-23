import FWCore.ParameterSet.Config as cms

def edmtest_GetTriggerNamesAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::GetTriggerNamesAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
