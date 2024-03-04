import FWCore.ParameterSet.Config as cms

def GaussRandomPThetaGunProducer(**kwargs):
  mod = cms.EDProducer('GaussRandomPThetaGunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
