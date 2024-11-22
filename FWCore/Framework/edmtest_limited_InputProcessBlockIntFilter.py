import FWCore.ParameterSet.Config as cms

def edmtest_limited_InputProcessBlockIntFilter(*args, **kwargs):
  mod = cms.EDFilter('edmtest::limited::InputProcessBlockIntFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
