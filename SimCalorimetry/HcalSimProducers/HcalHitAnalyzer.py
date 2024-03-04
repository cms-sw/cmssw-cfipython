import FWCore.ParameterSet.Config as cms

def HcalHitAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalHitAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
