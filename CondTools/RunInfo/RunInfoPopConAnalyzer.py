import FWCore.ParameterSet.Config as cms

def RunInfoPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('RunInfoPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
