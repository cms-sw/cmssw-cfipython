import FWCore.ParameterSet.Config as cms

gemOfflineMonitor = cms.EDProducer('GEMOfflineMonitor',
  digiTag = cms.InputTag('muonGEMDigis'),
  recHitTag = cms.InputTag('gemRecHits'),
  logCategory = cms.untracked.string('GEMOfflineMonitor'),
  mightGet = cms.optional.untracked.vstring
)
