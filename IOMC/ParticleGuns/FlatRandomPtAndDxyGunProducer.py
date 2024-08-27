import FWCore.ParameterSet.Config as cms

def FlatRandomPtAndDxyGunProducer(**kwargs):
  mod = cms.EDProducer('FlatRandomPtAndDxyGunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
