import FWCore.ParameterSet.Config as cms

def HcalGainsCheck(**kwargs):
  mod = cms.EDAnalyzer('HcalGainsCheck',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
