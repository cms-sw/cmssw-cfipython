import FWCore.ParameterSet.Config as cms

def HcalGainWidthsPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalGainWidthsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
