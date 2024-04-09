import FWCore.ParameterSet.Config as cms

def edmtest_limited_TestEndRunProducer(**kwargs):
  mod = cms.EDProducer('edmtest::limited::TestEndRunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod