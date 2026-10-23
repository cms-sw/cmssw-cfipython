import FWCore.ParameterSet.Config as cms

def CastorPedestalsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CastorPedestalsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
