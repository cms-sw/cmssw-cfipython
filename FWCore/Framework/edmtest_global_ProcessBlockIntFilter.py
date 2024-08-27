import FWCore.ParameterSet.Config as cms

def edmtest_global_ProcessBlockIntFilter(**kwargs):
  mod = cms.EDFilter('edmtest::global::ProcessBlockIntFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
