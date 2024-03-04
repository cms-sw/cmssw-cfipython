import FWCore.ParameterSet.Config as cms

def TtFullLepHypGenMatch(**kwargs):
  mod = cms.EDProducer('TtFullLepHypGenMatch',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
