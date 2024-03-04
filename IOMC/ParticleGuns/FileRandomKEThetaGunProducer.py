import FWCore.ParameterSet.Config as cms

def FileRandomKEThetaGunProducer(**kwargs):
  mod = cms.EDProducer('FileRandomKEThetaGunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
