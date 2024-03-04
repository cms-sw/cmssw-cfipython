import FWCore.ParameterSet.Config as cms

def edmtest_limited_InputProcessBlockIntFilter(**kwargs):
  mod = cms.EDFilter('edmtest::limited::InputProcessBlockIntFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
