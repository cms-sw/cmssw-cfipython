import FWCore.ParameterSet.Config as cms

btlDigiHitsDefaultValid = cms.EDProducer('BtlDigiHitsValidation',
  folder = cms.string('MTD/BTL/DigiHits'),
  inputTag = cms.InputTag('mix', 'FTLBarrel'),
  optionalPlots = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
