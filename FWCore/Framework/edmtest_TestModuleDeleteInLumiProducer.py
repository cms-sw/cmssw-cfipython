import FWCore.ParameterSet.Config as cms

def edmtest_TestModuleDeleteInLumiProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::TestModuleDeleteInLumiProducer',
    srcBeginProcess = cms.untracked.VInputTag(),
    srcBeginRun = cms.untracked.VInputTag(),
    srcBeginLumi = cms.untracked.VInputTag(),
    srcEvent = cms.untracked.VInputTag(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
