import FWCore.ParameterSet.Config as cms

hgcalCheckToolDigiEE = cms.EDAnalyzer('HGCalRecHitToolsPartialWafer',
  source = cms.InputTag('simHGCalUnsuppressedDigis', 'EE'),
  nameSense = cms.string('HGCalEESensitive'),
  checkDigi = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
