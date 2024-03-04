import FWCore.ParameterSet.Config as cms

def edmtest_TestModuleDeleteProducer(**kwargs):
  mod = cms.EDProducer('edmtest::TestModuleDeleteProducer',
    srcBeginProcess = cms.untracked.VInputTag(),
    srcBeginRun = cms.untracked.VInputTag(),
    srcBeginLumi = cms.untracked.VInputTag(),
    srcEvent = cms.untracked.VInputTag(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
