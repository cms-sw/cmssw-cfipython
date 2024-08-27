import FWCore.ParameterSet.Config as cms

def edmtest_global_TestEndRunProducer(**kwargs):
  mod = cms.EDProducer('edmtest::global::TestEndRunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
