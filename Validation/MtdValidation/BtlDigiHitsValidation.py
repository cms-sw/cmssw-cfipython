import FWCore.ParameterSet.Config as cms

def BtlDigiHitsValidation(*args, **kwargs):
  mod = cms.EDProducer('BtlDigiHitsValidation',
    folder = cms.string('MTD/BTL/DigiHits'),
    inputTag = cms.InputTag('mix', 'FTLBarrel'),
    optionalPlots = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
