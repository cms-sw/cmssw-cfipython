import FWCore.ParameterSet.Config as cms

def edmtest_GlobalIntProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::GlobalIntProducer',
    value = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
