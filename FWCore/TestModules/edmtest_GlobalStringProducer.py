import FWCore.ParameterSet.Config as cms

def edmtest_GlobalStringProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::GlobalStringProducer',
    value = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
