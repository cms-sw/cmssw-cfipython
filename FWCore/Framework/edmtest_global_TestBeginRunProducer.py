import FWCore.ParameterSet.Config as cms

def edmtest_global_TestBeginRunProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::global::TestBeginRunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
