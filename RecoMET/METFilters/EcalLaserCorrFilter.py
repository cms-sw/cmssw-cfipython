import FWCore.ParameterSet.Config as cms

def EcalLaserCorrFilter(*args, **kwargs):
  mod = cms.EDFilter('EcalLaserCorrFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
