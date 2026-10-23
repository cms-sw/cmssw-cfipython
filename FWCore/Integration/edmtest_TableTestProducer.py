import FWCore.ParameterSet.Config as cms

def edmtest_TableTestProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::TableTestProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
