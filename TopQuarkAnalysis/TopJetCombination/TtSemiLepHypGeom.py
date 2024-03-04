import FWCore.ParameterSet.Config as cms

def TtSemiLepHypGeom(**kwargs):
  mod = cms.EDProducer('TtSemiLepHypGeom',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
