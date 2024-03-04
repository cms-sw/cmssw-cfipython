import FWCore.ParameterSet.Config as cms

def HcalDcsMapPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalDcsMapPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
