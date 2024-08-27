import FWCore.ParameterSet.Config as cms

def RPCSeedGenerator(**kwargs):
  mod = cms.EDProducer('RPCSeedGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
