import FWCore.ParameterSet.Config as cms

def ResolutionAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ResolutionAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
