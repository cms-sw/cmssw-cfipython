import FWCore.ParameterSet.Config as cms

def edmtest_one_RunCacheProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::one::RunCacheProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
