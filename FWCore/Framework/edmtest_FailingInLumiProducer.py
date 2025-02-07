import FWCore.ParameterSet.Config as cms

def edmtest_FailingInLumiProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::FailingInLumiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
