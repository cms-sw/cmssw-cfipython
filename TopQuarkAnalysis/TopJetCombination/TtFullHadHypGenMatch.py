import FWCore.ParameterSet.Config as cms

def TtFullHadHypGenMatch(*args, **kwargs):
  mod = cms.EDProducer('TtFullHadHypGenMatch',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
