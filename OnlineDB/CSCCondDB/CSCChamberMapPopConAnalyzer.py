import FWCore.ParameterSet.Config as cms

def CSCChamberMapPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCChamberMapPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
