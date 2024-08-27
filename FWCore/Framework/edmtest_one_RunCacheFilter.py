import FWCore.ParameterSet.Config as cms

def edmtest_one_RunCacheFilter(**kwargs):
  mod = cms.EDFilter('edmtest::one::RunCacheFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
