import FWCore.ParameterSet.Config as cms

def HcalPedestalsCheck(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalPedestalsCheck',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
