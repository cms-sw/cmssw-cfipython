import FWCore.ParameterSet.Config as cms

def ExPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
