import FWCore.ParameterSet.Config as cms

def Analyzer_minbias(*args, **kwargs):
  mod = cms.EDAnalyzer('Analyzer_minbias',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
