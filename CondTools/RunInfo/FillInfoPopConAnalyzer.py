import FWCore.ParameterSet.Config as cms

def FillInfoPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('FillInfoPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
