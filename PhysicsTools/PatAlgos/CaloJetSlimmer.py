import FWCore.ParameterSet.Config as cms

def CaloJetSlimmer(**kwargs):
  mod = cms.EDProducer('CaloJetSlimmer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
