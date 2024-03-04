import FWCore.ParameterSet.Config as cms

def edmtest_limited_StreamIntFilter(**kwargs):
  mod = cms.EDFilter('edmtest::limited::StreamIntFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
