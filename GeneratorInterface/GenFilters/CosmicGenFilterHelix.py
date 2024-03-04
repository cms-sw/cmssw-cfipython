import FWCore.ParameterSet.Config as cms

def CosmicGenFilterHelix(**kwargs):
  mod = cms.EDFilter('CosmicGenFilterHelix',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
