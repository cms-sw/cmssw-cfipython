import FWCore.ParameterSet.Config as cms

def HcalZDCLowGainFractionsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalZDCLowGainFractionsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
