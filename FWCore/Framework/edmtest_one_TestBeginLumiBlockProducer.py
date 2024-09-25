import FWCore.ParameterSet.Config as cms

def edmtest_one_TestBeginLumiBlockProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::one::TestBeginLumiBlockProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
