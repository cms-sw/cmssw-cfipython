import FWCore.ParameterSet.Config as cms

def edmtest_global_TestEndProcessBlockFilter(**kwargs):
  mod = cms.EDFilter('edmtest::global::TestEndProcessBlockFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
