import FWCore.ParameterSet.Config as cms

def CastorGainsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CastorGainsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
