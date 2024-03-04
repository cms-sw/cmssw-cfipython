import FWCore.ParameterSet.Config as cms

def LHCInfoPerLSPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('LHCInfoPerLSPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
