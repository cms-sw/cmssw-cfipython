import FWCore.ParameterSet.Config as cms

def CastorGainsPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CastorGainsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
