import FWCore.ParameterSet.Config as cms

def edmtest_one_EndLumiBlockFilter(**kwargs):
  mod = cms.EDFilter('edmtest::one::EndLumiBlockFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
