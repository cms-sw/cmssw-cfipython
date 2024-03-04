import FWCore.ParameterSet.Config as cms

def CRackSeedGenerator(**kwargs):
  mod = cms.EDProducer('CRackSeedGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
