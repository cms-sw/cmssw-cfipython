import FWCore.ParameterSet.Config as cms

def edmtest_PythonTestProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::PythonTestProducer',
    source = cms.required.InputTag,
    inputVariable = cms.required.string,
    outputListVariable = cms.required.string,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
