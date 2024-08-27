import FWCore.ParameterSet.Config as cms

def edmtest_one_BeginRunFilter(**kwargs):
  mod = cms.EDFilter('edmtest::one::BeginRunFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
