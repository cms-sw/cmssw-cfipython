import FWCore.ParameterSet.Config as cms

def CosmicGenFilterHelix(*args, **kwargs):
  mod = cms.EDFilter('CosmicGenFilterHelix',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
