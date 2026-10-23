import FWCore.ParameterSet.Config as cms

def TestMergeResults(*args, **kwargs):
  mod = cms.EDAnalyzer('TestMergeResults',
    expectedBeginRunProd = cms.untracked.vint32(),
    expectedEndRunProd = cms.untracked.vint32(),
    expectedBeginLumiProd = cms.untracked.vint32(),
    expectedEndLumiProd = cms.untracked.vint32(),
    expectedBeginRunNew = cms.untracked.vint32(),
    expectedEndRunNew = cms.untracked.vint32(),
    expectedBeginLumiNew = cms.untracked.vint32(),
    expectedEndLumiNew = cms.untracked.vint32(),
    expectedEndRunProdImproperlyMerged = cms.untracked.vint32(),
    expectedEndLumiProdImproperlyMerged = cms.untracked.vint32(),
    expectedParents = cms.untracked.vstring(),
    expectedProcessHistoryInRuns = cms.untracked.vstring(),
    expectedDroppedEvent = cms.untracked.vint32(),
    expectedDroppedEvent1 = cms.untracked.vint32(),
    expectedDroppedEvent1NEvents = cms.untracked.vint32(),
    testAlias = cms.untracked.bool(False),
    verbose = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
