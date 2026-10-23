import FWCore.ParameterSet.Config as cms

def TtFullLepHypGenMatch(*args, **kwargs):
  mod = cms.EDProducer('TtFullLepHypGenMatch',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
