import FWCore.ParameterSet.Config as cms

def HcalPFCorrsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalPFCorrsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
