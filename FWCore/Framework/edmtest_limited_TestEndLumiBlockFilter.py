import FWCore.ParameterSet.Config as cms

def edmtest_limited_TestEndLumiBlockFilter(**kwargs):
  mod = cms.EDFilter('edmtest::limited::TestEndLumiBlockFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
