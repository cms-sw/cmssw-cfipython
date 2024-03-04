import FWCore.ParameterSet.Config as cms

def CSCBadWiresPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCBadWiresPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
