import FWCore.ParameterSet.Config as cms

def edmtest_one_BeginRunFilter(*args, **kwargs):
  mod = cms.EDFilter('edmtest::one::BeginRunFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
