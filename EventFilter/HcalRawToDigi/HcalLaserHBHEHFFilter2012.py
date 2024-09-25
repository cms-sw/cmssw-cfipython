import FWCore.ParameterSet.Config as cms

def HcalLaserHBHEHFFilter2012(*args, **kwargs):
  mod = cms.EDFilter('HcalLaserHBHEHFFilter2012',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
