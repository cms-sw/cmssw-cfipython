import FWCore.ParameterSet.Config as cms

def edmtest_limited_StreamIntProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::limited::StreamIntProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
