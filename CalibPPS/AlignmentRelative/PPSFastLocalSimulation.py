import FWCore.ParameterSet.Config as cms

def PPSFastLocalSimulation(**kwargs):
  mod = cms.EDProducer('PPSFastLocalSimulation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
