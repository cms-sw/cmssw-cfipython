import FWCore.ParameterSet.Config as cms

def HcalTimeCorrsPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalTimeCorrsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
