import FWCore.ParameterSet.Config as cms

def edmtest_one_LumiBlockCacheFilter(**kwargs):
  mod = cms.EDFilter('edmtest::one::LumiBlockCacheFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
