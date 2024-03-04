import FWCore.ParameterSet.Config as cms

def Analyzer_minbias(**kwargs):
  mod = cms.EDAnalyzer('Analyzer_minbias',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
