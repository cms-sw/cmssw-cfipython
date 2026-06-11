import FWCore.ParameterSet.Config as cms

def RunLumiEventAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('RunLumiEventAnalyzer',
    verbose = cms.untracked.bool(False),
    dumpTriggerResults = cms.untracked.bool(False),
    expectedEndingIndex = cms.untracked.int32(-1),
    expectedRunLumiEvents = cms.untracked.vuint64(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
