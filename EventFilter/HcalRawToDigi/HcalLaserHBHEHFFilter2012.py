import FWCore.ParameterSet.Config as cms

def HcalLaserHBHEHFFilter2012(**kwargs):
  mod = cms.EDFilter('HcalLaserHBHEHFFilter2012',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
