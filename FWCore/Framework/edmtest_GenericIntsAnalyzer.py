import FWCore.ParameterSet.Config as cms

def edmtest_GenericIntsAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('edmtest::GenericIntsAnalyzer',
    srcBeginProcess = cms.untracked.VInputTag(),
    srcBeginRun = cms.untracked.VInputTag(),
    srcBeginLumi = cms.untracked.VInputTag(),
    srcEvent = cms.untracked.VInputTag(),
    srcEndLumi = cms.untracked.VInputTag(),
    srcEndRun = cms.untracked.VInputTag(),
    srcEndProcess = cms.untracked.VInputTag(),
    inputShouldExist = cms.untracked.bool(False),
    inputShouldBeMissing = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
