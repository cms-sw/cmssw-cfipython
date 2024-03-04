import FWCore.ParameterSet.Config as cms

def FlatRandomPtThetaGunProducer(**kwargs):
  mod = cms.EDProducer('FlatRandomPtThetaGunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
