import FWCore.ParameterSet.Config as cms

def TtSemiLepHypGeom(*args, **kwargs):
  mod = cms.EDProducer('TtSemiLepHypGeom',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
