import FWCore.ParameterSet.Config as cms

def edmtest_one_TestBeginProcessBlockFilter(*args, **kwargs):
  mod = cms.EDFilter('edmtest::one::TestBeginProcessBlockFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
