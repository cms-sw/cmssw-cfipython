import FWCore.ParameterSet.Config as cms

def TestFindProduct(*args, **kwargs):
  mod = cms.EDAnalyzer('TestFindProduct',
    inputTags = cms.untracked.VInputTag(),
    expectedSum = cms.untracked.int32(0),
    expectedCache = cms.untracked.int32(0),
    getByTokenFirst = cms.untracked.bool(False),
    runProducerParameterCheck = cms.untracked.bool(False),
    testGetterOfProducts = cms.untracked.bool(False),
    inputTagsNotFound = cms.untracked.VInputTag(),
    inputTagsView = cms.untracked.VInputTag(),
    inputTagsUInt64 = cms.untracked.VInputTag(),
    inputTagsEndLumi = cms.untracked.VInputTag(),
    inputTagsEndRun = cms.untracked.VInputTag(),
    inputTagsBeginProcessBlock = cms.untracked.VInputTag(),
    inputTagsInputProcessBlock = cms.untracked.VInputTag(),
    inputTagsEndProcessBlock = cms.untracked.VInputTag(),
    inputTagsEndProcessBlock2 = cms.untracked.VInputTag(),
    inputTagsEndProcessBlock3 = cms.untracked.VInputTag(),
    inputTagsEndProcessBlock4 = cms.untracked.VInputTag(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
