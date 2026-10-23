import FWCore.ParameterSet.Config as cms

def edmtest_limited_StreamIntFilter(*args, **kwargs):
  mod = cms.EDFilter('edmtest::limited::StreamIntFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
