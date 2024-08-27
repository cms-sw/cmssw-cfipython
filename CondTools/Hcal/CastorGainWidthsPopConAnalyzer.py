import FWCore.ParameterSet.Config as cms

def CastorGainWidthsPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CastorGainWidthsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
