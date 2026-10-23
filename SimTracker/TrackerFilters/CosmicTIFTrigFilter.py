import FWCore.ParameterSet.Config as cms

def CosmicTIFTrigFilter(*args, **kwargs):
  mod = cms.EDFilter('CosmicTIFTrigFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
