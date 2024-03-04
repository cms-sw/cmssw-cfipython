import FWCore.ParameterSet.Config as cms

def GenJetBCEnergyRatio(**kwargs):
  mod = cms.EDProducer('GenJetBCEnergyRatio',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
