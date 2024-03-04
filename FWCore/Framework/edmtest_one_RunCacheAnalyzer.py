import FWCore.ParameterSet.Config as cms

def edmtest_one_RunCacheAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('edmtest::one::RunCacheAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
