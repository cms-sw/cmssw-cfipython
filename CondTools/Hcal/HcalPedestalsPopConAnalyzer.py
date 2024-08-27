import FWCore.ParameterSet.Config as cms

def HcalPedestalsPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalPedestalsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
