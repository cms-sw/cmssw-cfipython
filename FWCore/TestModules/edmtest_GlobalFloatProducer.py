import FWCore.ParameterSet.Config as cms

def edmtest_GlobalFloatProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::GlobalFloatProducer',
    value = cms.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
