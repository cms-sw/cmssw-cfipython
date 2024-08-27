import FWCore.ParameterSet.Config as cms

def edmtest_MustRunIntProducer(**kwargs):
  mod = cms.EDProducer('edmtest::MustRunIntProducer',
    ivalue = cms.required.int32,
    produce = cms.bool(True),
    mustRunEvent = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
