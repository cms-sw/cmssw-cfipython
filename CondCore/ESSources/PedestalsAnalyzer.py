import FWCore.ParameterSet.Config as cms

def PedestalsAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('PedestalsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
