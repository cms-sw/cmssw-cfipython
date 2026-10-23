import FWCore.ParameterSet.Config as cms

def edmtest_one_EndLumiBlockFilter(*args, **kwargs):
  mod = cms.EDFilter('edmtest::one::EndLumiBlockFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
