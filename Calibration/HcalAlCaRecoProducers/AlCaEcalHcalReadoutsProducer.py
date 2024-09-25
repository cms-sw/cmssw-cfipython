import FWCore.ParameterSet.Config as cms

def AlCaEcalHcalReadoutsProducer(*args, **kwargs):
  mod = cms.EDProducer('AlCaEcalHcalReadoutsProducer',
    hbheInput = cms.InputTag('hbhereco'),
    hfInput = cms.InputTag('hfreco'),
    hoInput = cms.InputTag('horeco'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
