import FWCore.ParameterSet.Config as cms

def edmtest_FailingInRunProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::FailingInRunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
