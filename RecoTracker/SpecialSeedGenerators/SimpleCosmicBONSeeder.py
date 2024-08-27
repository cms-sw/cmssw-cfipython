import FWCore.ParameterSet.Config as cms

def SimpleCosmicBONSeeder(**kwargs):
  mod = cms.EDProducer('SimpleCosmicBONSeeder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
