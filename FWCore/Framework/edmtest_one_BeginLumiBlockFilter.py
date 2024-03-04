import FWCore.ParameterSet.Config as cms

def edmtest_one_BeginLumiBlockFilter(**kwargs):
  mod = cms.EDFilter('edmtest::one::BeginLumiBlockFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
