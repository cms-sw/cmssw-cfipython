import FWCore.ParameterSet.Config as cms

def edmtest_limited_TestBeginLumiBlockProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::limited::TestBeginLumiBlockProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
