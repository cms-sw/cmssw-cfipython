import FWCore.ParameterSet.Config as cms

def BeamMomentumGunProducer(**kwargs):
  mod = cms.EDProducer('BeamMomentumGunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
