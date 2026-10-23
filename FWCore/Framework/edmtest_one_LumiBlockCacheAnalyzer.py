import FWCore.ParameterSet.Config as cms

def edmtest_one_LumiBlockCacheAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::one::LumiBlockCacheAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
