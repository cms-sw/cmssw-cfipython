import FWCore.ParameterSet.Config as cms

def edmtest_global_TestEndRunProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::global::TestEndRunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
