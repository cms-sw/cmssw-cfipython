import FWCore.ParameterSet.Config as cms

def TestReadTriggerEvent(**kwargs):
  mod = cms.EDAnalyzer('TestReadTriggerEvent',
    expectedUsedProcessName = cms.required.string,
    expectedCollectionTags = cms.required.vstring,
    expectedCollectionKeys = cms.required.vuint32,
    expectedIds = cms.required.vint32,
    expectedPts = cms.required.vdouble,
    expectedEtas = cms.required.vdouble,
    expectedPhis = cms.required.vdouble,
    expectedMasses = cms.required.vdouble,
    expectedFilterTags = cms.required.vstring,
    expectedElementsPerVector = cms.required.uint32,
    expectedFilterIds = cms.required.vint32,
    expectedFilterKeys = cms.required.vuint32,
    triggerEventTag = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod