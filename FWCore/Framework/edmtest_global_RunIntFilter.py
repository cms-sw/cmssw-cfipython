import FWCore.ParameterSet.Config as cms

def edmtest_global_RunIntFilter(*args, **kwargs):
  mod = cms.EDFilter('edmtest::global::RunIntFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
