import FWCore.ParameterSet.Config as cms

def GenJetBCEnergyRatio(*args, **kwargs):
  mod = cms.EDProducer('GenJetBCEnergyRatio',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
