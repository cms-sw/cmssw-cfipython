import FWCore.ParameterSet.Config as cms

def HcalPedestalsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalPedestalsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
