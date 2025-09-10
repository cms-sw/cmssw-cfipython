import FWCore.ParameterSet.Config as cms

def CastorGainWidthsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CastorGainWidthsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
