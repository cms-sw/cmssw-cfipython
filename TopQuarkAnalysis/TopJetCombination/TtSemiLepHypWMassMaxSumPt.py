import FWCore.ParameterSet.Config as cms

def TtSemiLepHypWMassMaxSumPt(**kwargs):
  mod = cms.EDProducer('TtSemiLepHypWMassMaxSumPt',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
