import FWCore.ParameterSet.Config as cms

def ESTestAnalyzerAZ(**kwargs):
  mod = cms.EDAnalyzer('ESTestAnalyzerAZ',
    runsToGetDataFor = cms.required.vint32,
    expectedValuesA = cms.untracked.vint32(),
    expectedValuesZ = cms.untracked.vint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
