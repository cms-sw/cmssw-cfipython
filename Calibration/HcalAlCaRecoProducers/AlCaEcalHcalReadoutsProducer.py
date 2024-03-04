import FWCore.ParameterSet.Config as cms

def AlCaEcalHcalReadoutsProducer(**kwargs):
  mod = cms.EDProducer('AlCaEcalHcalReadoutsProducer',
    hbheInput = cms.InputTag('hbhereco'),
    hfInput = cms.InputTag('hfreco'),
    hoInput = cms.InputTag('horeco'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
