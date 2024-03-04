import FWCore.ParameterSet.Config as cms

def HcalRespCorrsPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalRespCorrsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
