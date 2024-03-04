import FWCore.ParameterSet.Config as cms

def HcalQIETypesPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalQIETypesPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
