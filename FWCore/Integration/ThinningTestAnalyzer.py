import FWCore.ParameterSet.Config as cms

def ThinningTestAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ThinningTestAnalyzer',
    parentTag = cms.required.InputTag,
    thinnedTag = cms.required.InputTag,
    associationTag = cms.required.InputTag,
    trackTag = cms.required.InputTag,
    parentWasDropped = cms.bool(False),
    thinnedWasDropped = cms.bool(False),
    thinnedIsAlias = cms.bool(False),
    refToParentIsAvailable = cms.bool(True),
    expectedParentContent = cms.vint32(),
    expectedThinnedContent = cms.vint32(),
    expectedIndexesIntoParent = cms.vuint32(),
    associationShouldBeDropped = cms.bool(False),
    expectedValues = cms.required.vint32,
    parentSlimmedCount = cms.int32(0),
    thinnedSlimmedCount = cms.int32(0),
    refSlimmedCount = cms.int32(0),
    slimmedValueFactor = cms.int32(10),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
