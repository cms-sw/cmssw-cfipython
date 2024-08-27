import FWCore.ParameterSet.Config as cms

def CosmicTIFTrigFilter(**kwargs):
  mod = cms.EDFilter('CosmicTIFTrigFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
