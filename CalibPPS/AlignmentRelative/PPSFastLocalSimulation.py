import FWCore.ParameterSet.Config as cms

def PPSFastLocalSimulation(*args, **kwargs):
  mod = cms.EDProducer('PPSFastLocalSimulation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
