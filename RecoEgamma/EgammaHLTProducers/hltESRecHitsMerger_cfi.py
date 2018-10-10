import FWCore.ParameterSet.Config as cms

hltESRecHitsMerger = cms.EDProducer('ESRecHitsMerger',
  debug = cms.bool(False),
  EgammaSource_ES = cms.InputTag('dummyEgamma'),
  MuonsSource_ES = cms.InputTag('dummyMuons'),
  TausSource_ES = cms.InputTag('dummyTaus'),
  JetsSource_ES = cms.InputTag('dummyJets'),
  RestSource_ES = cms.InputTag('dummyRest'),
  Pi0Source_ES = cms.InputTag('dummyPi0'),
  EtaSource_ES = cms.InputTag('dummyEta'),
  OutputLabel_ES = cms.string('EcalRecHitsES'),
  EcalRecHitCollectionES = cms.string('EcalRecHitsES')
)
