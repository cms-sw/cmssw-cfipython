import FWCore.ParameterSet.Config as cms

def SimTauAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('SimTauAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
