import FWCore.ParameterSet.Config as cms

def edmtest_one_LumiBlockCacheFilter(*args, **kwargs):
  mod = cms.EDFilter('edmtest::one::LumiBlockCacheFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
