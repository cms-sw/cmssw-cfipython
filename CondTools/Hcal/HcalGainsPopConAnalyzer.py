import FWCore.ParameterSet.Config as cms

def HcalGainsPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalGainsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
