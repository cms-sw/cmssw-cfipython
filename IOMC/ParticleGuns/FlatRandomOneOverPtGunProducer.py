import FWCore.ParameterSet.Config as cms

def FlatRandomOneOverPtGunProducer(**kwargs):
  mod = cms.EDProducer('FlatRandomOneOverPtGunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
