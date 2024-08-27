import FWCore.ParameterSet.Config as cms

def PATJetSlimmer(**kwargs):
  mod = cms.EDProducer('PATJetSlimmer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
