import FWCore.ParameterSet.Config as cms

def AnalyzerPrintGeomInfo(*args, **kwargs):
  mod = cms.EDAnalyzer('AnalyzerPrintGeomInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
