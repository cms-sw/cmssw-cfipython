import FWCore.ParameterSet.Config as cms

def HcalHPDFilter(*args, **kwargs):
  mod = cms.EDFilter('HcalHPDFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod