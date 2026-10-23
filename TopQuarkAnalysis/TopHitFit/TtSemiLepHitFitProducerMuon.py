import FWCore.ParameterSet.Config as cms

def TtSemiLepHitFitProducerMuon(*args, **kwargs):
  mod = cms.EDProducer('TtSemiLepHitFitProducerMuon',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
