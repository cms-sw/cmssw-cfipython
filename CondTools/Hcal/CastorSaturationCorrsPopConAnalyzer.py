import FWCore.ParameterSet.Config as cms

def CastorSaturationCorrsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CastorSaturationCorrsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
