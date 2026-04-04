import FWCore.ParameterSet.Config as cms

def HcalTimeCorrsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalTimeCorrsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
