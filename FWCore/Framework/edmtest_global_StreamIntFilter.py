import FWCore.ParameterSet.Config as cms

def edmtest_global_StreamIntFilter(**kwargs):
  mod = cms.EDFilter('edmtest::global::StreamIntFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
