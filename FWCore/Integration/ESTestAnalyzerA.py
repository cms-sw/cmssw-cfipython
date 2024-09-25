import FWCore.ParameterSet.Config as cms

def ESTestAnalyzerA(*args, **kwargs):
  mod = cms.EDAnalyzer('ESTestAnalyzerA',
    runsToGetDataFor = cms.required.vint32,
    expectedValues = cms.untracked.vint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
