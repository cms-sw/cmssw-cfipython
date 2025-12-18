import FWCore.ParameterSet.Config as cms

def edmtest_EventIDProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::EventIDProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
