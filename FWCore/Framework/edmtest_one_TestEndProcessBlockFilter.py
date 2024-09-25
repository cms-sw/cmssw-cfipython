import FWCore.ParameterSet.Config as cms

def edmtest_one_TestEndProcessBlockFilter(*args, **kwargs):
  mod = cms.EDFilter('edmtest::one::TestEndProcessBlockFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
