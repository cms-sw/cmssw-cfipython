import FWCore.ParameterSet.Config as cms

def EcalBasicUncalibRecHitFilter(*args, **kwargs):
  mod = cms.EDFilter('EcalBasicUncalibRecHitFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
