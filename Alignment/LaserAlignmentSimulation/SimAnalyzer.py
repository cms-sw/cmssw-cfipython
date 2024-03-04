import FWCore.ParameterSet.Config as cms

def SimAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('SimAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
