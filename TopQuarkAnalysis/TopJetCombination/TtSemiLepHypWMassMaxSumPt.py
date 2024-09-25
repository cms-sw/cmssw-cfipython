import FWCore.ParameterSet.Config as cms

def TtSemiLepHypWMassMaxSumPt(*args, **kwargs):
  mod = cms.EDProducer('TtSemiLepHypWMassMaxSumPt',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
