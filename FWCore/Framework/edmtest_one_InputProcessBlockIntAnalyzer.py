import FWCore.ParameterSet.Config as cms

def edmtest_one_InputProcessBlockIntAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::one::InputProcessBlockIntAnalyzer',
    transitions = cms.required.int32,
    expectedByRun = cms.vint32(),
    expectedSum = cms.required.int32,
    expectedFillerSum = cms.untracked.int32(0),
    expectedCacheSize = cms.untracked.uint32(0),
    consumesBeginProcessBlock = cms.InputTag(''),
    consumesEndProcessBlock = cms.InputTag(''),
    consumesBeginProcessBlockM = cms.InputTag(''),
    consumesEndProcessBlockM = cms.InputTag(''),
    consumesBeginProcessBlockNotFound = cms.InputTag(''),
    consumesEndProcessBlockNotFound = cms.InputTag(''),
    consumesProcessBlockNotFound1 = cms.InputTag(''),
    consumesProcessBlockNotFound2 = cms.InputTag(''),
    consumesProcessBlockNotFound3 = cms.InputTag(''),
    consumesProcessBlockNotFound4 = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
