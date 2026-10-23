import FWCore.ParameterSet.Config as cms

def HcalZSThresholdsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalZSThresholdsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
