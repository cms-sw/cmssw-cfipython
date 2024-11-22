import FWCore.ParameterSet.Config as cms

def TestReadGlobalObjectMapRecord(*args, **kwargs):
  mod = cms.EDAnalyzer('TestReadGlobalObjectMapRecord',
    expectedAlgoNames = cms.required.vstring,
    expectedAlgoBitNumbers = cms.required.vint32,
    expectedAlgoGtlResults = cms.required.vint32,
    expectedTokenNames0 = cms.required.vstring,
    expectedTokenNumbers0 = cms.required.vint32,
    expectedTokenResults0 = cms.required.vint32,
    expectedTokenNames3 = cms.required.vstring,
    expectedTokenNumbers3 = cms.required.vint32,
    expectedTokenResults3 = cms.required.vint32,
    expectedFirstElement = cms.required.int32,
    expectedElementDelta = cms.required.int32,
    expectedFinalValue = cms.required.int32,
    globalObjectMapRecordTag = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
