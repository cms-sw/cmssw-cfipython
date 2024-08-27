import FWCore.ParameterSet.Config as cms

def TtSemiLepHypHitFit(**kwargs):
  mod = cms.EDProducer('TtSemiLepHypHitFit',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
