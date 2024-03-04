import FWCore.ParameterSet.Config as cms

def edmtest_TestModuleDeleteAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('edmtest::TestModuleDeleteAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
