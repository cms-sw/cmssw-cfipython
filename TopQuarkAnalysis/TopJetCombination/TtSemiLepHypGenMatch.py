import FWCore.ParameterSet.Config as cms

def TtSemiLepHypGenMatch(**kwargs):
  mod = cms.EDProducer('TtSemiLepHypGenMatch',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
