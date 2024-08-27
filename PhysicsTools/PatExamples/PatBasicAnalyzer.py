import FWCore.ParameterSet.Config as cms

def PatBasicAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('PatBasicAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
