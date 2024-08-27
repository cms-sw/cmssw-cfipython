import FWCore.ParameterSet.Config as cms

def CastorSaturationCorrsPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CastorSaturationCorrsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
