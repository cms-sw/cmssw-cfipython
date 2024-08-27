import FWCore.ParameterSet.Config as cms

def HcalFrontEndMapPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalFrontEndMapPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
