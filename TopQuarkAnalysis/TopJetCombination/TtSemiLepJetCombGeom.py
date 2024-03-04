import FWCore.ParameterSet.Config as cms

def TtSemiLepJetCombGeom(**kwargs):
  mod = cms.EDProducer('TtSemiLepJetCombGeom',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
