import FWCore.ParameterSet.Config as cms

def CaloNavigationAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CaloNavigationAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
