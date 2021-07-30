import FWCore.ParameterSet.Config as cms

GEMRecHitSource = cms.EDProducer('GEMRecHitSource',
  recHitsInputLabel = cms.InputTag('gemRecHits'),
  idxFirstDigi = cms.int32(0),
  ClusterSizeBinNum = cms.int32(9),
  modeRelVal = cms.bool(False),
  logCategory = cms.untracked.string('GEMRecHitSource'),
  mightGet = cms.optional.untracked.vstring
)
