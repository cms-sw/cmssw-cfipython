import FWCore.ParameterSet.Config as cms

def EcalBasicUncalibRecHitFilter(**kwargs):
  mod = cms.EDFilter('EcalBasicUncalibRecHitFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
