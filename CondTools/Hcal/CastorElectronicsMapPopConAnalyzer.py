import FWCore.ParameterSet.Config as cms

def CastorElectronicsMapPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CastorElectronicsMapPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
