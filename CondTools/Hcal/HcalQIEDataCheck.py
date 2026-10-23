import FWCore.ParameterSet.Config as cms

def HcalQIEDataCheck(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalQIEDataCheck',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
