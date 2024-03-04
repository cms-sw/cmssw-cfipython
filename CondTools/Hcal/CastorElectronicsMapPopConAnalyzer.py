import FWCore.ParameterSet.Config as cms

def CastorElectronicsMapPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CastorElectronicsMapPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
