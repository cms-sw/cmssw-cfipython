import FWCore.ParameterSet.Config as cms

def ESTestAnalyzerAZ(*args, **kwargs):
  mod = cms.EDAnalyzer('ESTestAnalyzerAZ',
    runsToGetDataFor = cms.required.vint32,
    expectedValuesA = cms.untracked.vint32(),
    expectedValuesZ = cms.untracked.vint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
