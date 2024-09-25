import FWCore.ParameterSet.Config as cms

def HcalLaserEventFilter2012(*args, **kwargs):
  mod = cms.EDFilter('HcalLaserEventFilter2012',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
