import FWCore.ParameterSet.Config as cms

def edmtest_global_RunIntFilter(**kwargs):
  mod = cms.EDFilter('edmtest::global::RunIntFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
