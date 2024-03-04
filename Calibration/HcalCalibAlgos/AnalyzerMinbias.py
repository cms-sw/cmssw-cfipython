import FWCore.ParameterSet.Config as cms

def AnalyzerMinbias(**kwargs):
  mod = cms.EDAnalyzer('AnalyzerMinbias',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
