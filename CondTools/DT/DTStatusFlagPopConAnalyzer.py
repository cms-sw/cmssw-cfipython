import FWCore.ParameterSet.Config as cms

def DTStatusFlagPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('DTStatusFlagPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
