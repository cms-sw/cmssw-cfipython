import FWCore.ParameterSet.Config as cms

def TtSemiLepHitFitProducerMuon(**kwargs):
  mod = cms.EDProducer('TtSemiLepHitFitProducerMuon',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
