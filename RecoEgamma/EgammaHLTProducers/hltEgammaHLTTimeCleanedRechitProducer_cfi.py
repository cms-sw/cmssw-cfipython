import FWCore.ParameterSet.Config as cms

hltEgammaHLTTimeCleanedRechitProducer = cms.EDProducer('EgammaHLTTimeCleanedRechitProducer',
  productLabels = cms.vstring(
    'EcalTimeCleanedRecHitsEB',
    'EcalTimeCleanedRecHitsEE'
  ),
  ecalhitLabels = cms.VInputTag(
    'hltEcalRecHitAll:EcalRecHitsEB',
    'hltEcalRecHitAll:EcalRecHitsEE'
  ),
  TimeMax = cms.double(10),
  TimeMin = cms.double(-10)
)
