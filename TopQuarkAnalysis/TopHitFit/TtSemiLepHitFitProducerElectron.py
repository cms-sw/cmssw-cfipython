import FWCore.ParameterSet.Config as cms

def TtSemiLepHitFitProducerElectron(*args, **kwargs):
  mod = cms.EDProducer('TtSemiLepHitFitProducerElectron',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
