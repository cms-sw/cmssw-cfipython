import FWCore.ParameterSet.Config as cms

def edmtest_GlobalVectorProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::GlobalVectorProducer',
    values = cms.vdouble(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
