import FWCore.ParameterSet.Config as cms

def edmtest_PythonTestProducer(**kwargs):
  mod = cms.EDProducer('edmtest::PythonTestProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
