import FWCore.ParameterSet.Config as cms

hltEcalRecHitsMerger = cms.EDProducer('EcalRecHitsMerger',
  debug = cms.bool(False),
  EgammaSource_EB = cms.InputTag('ecalRegionalEgammaRecHitTmp', 'EcalRecHitsEB'),
  MuonsSource_EB = cms.InputTag('ecalRegionalMuonsRecHitTmp', 'EcalRecHitsEB'),
  TausSource_EB = cms.InputTag('ecalRegionalTausRecHitTmp', 'EcalRecHitsEB'),
  JetsSource_EB = cms.InputTag('ecalRegionalJetsRecHitTmp', 'EcalRecHitsEB'),
  RestSource_EB = cms.InputTag('ecalRegionalRestRecHitTmp', 'EcalRecHitsEB'),
  Pi0Source_EB = cms.InputTag('dummyPi0'),
  EgammaSource_EE = cms.InputTag('ecalRegionalEgammaRecHitTmp', 'EcalRecHitsEE'),
  MuonsSource_EE = cms.InputTag('ecalRegionalMuonsRecHitTmp', 'EcalRecHitsEE'),
  TausSource_EE = cms.InputTag('ecalRegionalTausRecHitTmp', 'EcalRecHitsEE'),
  JetsSource_EE = cms.InputTag('ecalRegionalJetsRecHitTmp', 'EcalRecHitsEE'),
  RestSource_EE = cms.InputTag('ecalRegionalRestRecHitTmp', 'EcalRecHitsEE'),
  Pi0Source_EE = cms.InputTag('dummyPi0'),
  OutputLabel_EB = cms.string('EcalRecHitsEB'),
  OutputLabel_EE = cms.string('EcalRecHitsEE'),
  EcalRecHitCollectionEB = cms.string('EcalRecHitsEB'),
  EcalRecHitCollectionEE = cms.string('EcalRecHitsEE')
)
