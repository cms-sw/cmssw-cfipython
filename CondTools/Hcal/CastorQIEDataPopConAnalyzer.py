import FWCore.ParameterSet.Config as cms

def CastorQIEDataPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CastorQIEDataPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
