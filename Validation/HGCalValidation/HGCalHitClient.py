import FWCore.ParameterSet.Config as cms

def HGCalHitClient(**kwargs):
  mod = cms.EDProducer('HGCalHitClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
