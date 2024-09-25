import FWCore.ParameterSet.Config as cms

def HcalConditionsTest(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalConditionsTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
