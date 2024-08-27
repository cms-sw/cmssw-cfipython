import FWCore.ParameterSet.Config as cms

def CSCCrateMapPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCCrateMapPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
