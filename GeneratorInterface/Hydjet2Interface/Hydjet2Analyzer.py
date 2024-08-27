import FWCore.ParameterSet.Config as cms

def Hydjet2Analyzer(**kwargs):
  mod = cms.EDAnalyzer('Hydjet2Analyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
