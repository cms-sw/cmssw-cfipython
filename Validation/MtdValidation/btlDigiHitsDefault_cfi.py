import FWCore.ParameterSet.Config as cms

btlDigiHitsDefault = cms.EDProducer('BtlDigiHitsValidation',
  folder = cms.string('MTD/BTL/DigiHits'),
  inputTag = cms.InputTag('mix', 'FTLBarrel'),
  mightGet = cms.optional.untracked.vstring
)
