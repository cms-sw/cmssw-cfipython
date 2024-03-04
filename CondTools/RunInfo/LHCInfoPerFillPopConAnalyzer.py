import FWCore.ParameterSet.Config as cms

def LHCInfoPerFillPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('LHCInfoPerFillPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
