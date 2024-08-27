import FWCore.ParameterSet.Config as cms

def HcalPedestalsCheck(**kwargs):
  mod = cms.EDAnalyzer('HcalPedestalsCheck',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
