import FWCore.ParameterSet.Config as cms

def edmtest_limited_TestEndRunFilter(*args, **kwargs):
  mod = cms.EDFilter('edmtest::limited::TestEndRunFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
