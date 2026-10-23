import FWCore.ParameterSet.Config as cms

def HcalRespCorrsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalRespCorrsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
