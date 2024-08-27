import FWCore.ParameterSet.Config as cms

def edmtest_limited_TestEndLumiBlockProducer(**kwargs):
  mod = cms.EDProducer('edmtest::limited::TestEndLumiBlockProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
