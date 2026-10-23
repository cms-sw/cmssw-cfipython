import FWCore.ParameterSet.Config as cms

def edmtest_one_TestEndLumiBlockProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::one::TestEndLumiBlockProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
