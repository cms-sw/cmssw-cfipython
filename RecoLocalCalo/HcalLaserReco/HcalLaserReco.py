import FWCore.ParameterSet.Config as cms

def HcalLaserReco(**kwargs):
  mod = cms.EDProducer('HcalLaserReco',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
