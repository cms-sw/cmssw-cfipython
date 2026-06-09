import FWCore.ParameterSet.Config as cms

def HistoryAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HistoryAnalyzer',
    expectedSize = cms.required.int32,
    expectedCount = cms.required.int32,
    expectedSelectEventsInfo = cms.required.VPSet,
    expectedPaths = cms.required.vstring,
    expectedEndPaths = cms.required.vstring,
    expectedModules = cms.required.vstring,
    expectedDroppedEndPaths = cms.required.vstring,
    expectedDroppedModules = cms.required.vstring,
    expectedDropFromProcPSet = cms.required.vstring,
    expectedModulesOnEndPaths = cms.PSet(
      allowAnyLabel_ = cms.optional.vstring
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
