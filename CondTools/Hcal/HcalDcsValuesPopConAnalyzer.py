import FWCore.ParameterSet.Config as cms

def HcalDcsValuesPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalDcsValuesPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
