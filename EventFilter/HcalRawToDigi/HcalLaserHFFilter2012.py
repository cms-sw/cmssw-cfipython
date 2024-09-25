import FWCore.ParameterSet.Config as cms

def HcalLaserHFFilter2012(*args, **kwargs):
  mod = cms.EDFilter('HcalLaserHFFilter2012',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
