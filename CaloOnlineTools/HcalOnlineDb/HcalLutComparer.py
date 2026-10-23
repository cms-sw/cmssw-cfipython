import FWCore.ParameterSet.Config as cms

def HcalLutComparer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalLutComparer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
