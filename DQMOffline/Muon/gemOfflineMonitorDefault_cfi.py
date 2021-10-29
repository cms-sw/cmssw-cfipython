import FWCore.ParameterSet.Config as cms

gemOfflineMonitorDefault = cms.EDProducer('GEMOfflineMonitor',
  digiTag = cms.InputTag('muonGEMDigis'),
  recHitTag = cms.InputTag('gemRecHits'),
  logCategory = cms.untracked.string('GEMOfflineMonitor'),
  doDigiOccupancy = cms.untracked.bool(True),
  doHitOccupancy = cms.untracked.bool(True),
  mightGet = cms.optional.untracked.vstring
)
