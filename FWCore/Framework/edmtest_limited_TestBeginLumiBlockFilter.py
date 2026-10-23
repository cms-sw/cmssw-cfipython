import FWCore.ParameterSet.Config as cms

def edmtest_limited_TestBeginLumiBlockFilter(*args, **kwargs):
  mod = cms.EDFilter('edmtest::limited::TestBeginLumiBlockFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
