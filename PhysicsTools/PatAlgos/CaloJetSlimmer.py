import FWCore.ParameterSet.Config as cms

def CaloJetSlimmer(*args, **kwargs):
  mod = cms.EDProducer('CaloJetSlimmer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
