import FWCore.ParameterSet.Config as cms

def CastorDigiAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CastorDigiAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
