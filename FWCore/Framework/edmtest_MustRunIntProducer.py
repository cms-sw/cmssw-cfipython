import FWCore.ParameterSet.Config as cms

def edmtest_MustRunIntProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::MustRunIntProducer',
    ivalue = cms.required.int32,
    produce = cms.bool(True),
    mustRunEvent = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
