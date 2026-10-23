import FWCore.ParameterSet.Config as cms

def edmtest_global_LumiIntFilter(*args, **kwargs):
  mod = cms.EDFilter('edmtest::global::LumiIntFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
