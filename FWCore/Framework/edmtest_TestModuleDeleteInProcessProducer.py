import FWCore.ParameterSet.Config as cms

def edmtest_TestModuleDeleteInProcessProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::TestModuleDeleteInProcessProducer',
    srcBeginRun = cms.untracked.VInputTag(),
    srcBeginLumi = cms.untracked.VInputTag(),
    srcEvent = cms.untracked.VInputTag(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
