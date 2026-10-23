import FWCore.ParameterSet.Config as cms

def HGCalTBCheckGunPostion(*args, **kwargs):
  mod = cms.EDFilter('HGCalTBCheckGunPostion',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
