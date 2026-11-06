import FWCore.ParameterSet.Config as cms

def BtlDigiSoAHitsValidation(*args, **kwargs):
  mod = cms.EDProducer('BtlDigiSoAHitsValidation',
    folder = cms.string('MTD/BTL/DigiHitsSoA'),
    inputTag = cms.InputTag('btlDigiSoAProducer', 'MTDBarrelSoA'),
    optionalPlots = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
