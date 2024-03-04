import FWCore.ParameterSet.Config as cms

def EcalLaserCorrFilter(**kwargs):
  mod = cms.EDFilter('EcalLaserCorrFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
