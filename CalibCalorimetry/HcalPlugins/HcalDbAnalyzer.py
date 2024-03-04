import FWCore.ParameterSet.Config as cms

def HcalDbAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalDbAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
