import FWCore.ParameterSet.Config as cms

def BtlDigiHitsValidation(**kwargs):
  mod = cms.EDProducer('BtlDigiHitsValidation',
    folder = cms.string('MTD/BTL/DigiHits'),
    inputTag = cms.InputTag('mix', 'FTLBarrel'),
    optionalPlots = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
