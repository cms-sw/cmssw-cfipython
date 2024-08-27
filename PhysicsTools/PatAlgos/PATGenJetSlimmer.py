import FWCore.ParameterSet.Config as cms

def PATGenJetSlimmer(**kwargs):
  mod = cms.EDProducer('PATGenJetSlimmer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
