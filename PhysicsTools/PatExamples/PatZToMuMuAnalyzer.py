import FWCore.ParameterSet.Config as cms

def PatZToMuMuAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('PatZToMuMuAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
