import FWCore.ParameterSet.Config as cms

def CommonModeAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CommonModeAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
