import FWCore.ParameterSet.Config as cms

def ESTestAnalyzerA(**kwargs):
  mod = cms.EDAnalyzer('ESTestAnalyzerA',
    runsToGetDataFor = cms.required.vint32,
    expectedValues = cms.untracked.vint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
