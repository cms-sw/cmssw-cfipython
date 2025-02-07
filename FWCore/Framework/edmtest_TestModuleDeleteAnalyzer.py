import FWCore.ParameterSet.Config as cms

def edmtest_TestModuleDeleteAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::TestModuleDeleteAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
