import FWCore.ParameterSet.Config as cms

def PATPhotonSlimmer(**kwargs):
  mod = cms.EDProducer('PATPhotonSlimmer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
