import FWCore.ParameterSet.Config as cms

GEMRecHitSource = cms.EDProducer('GEMRecHitSource',
  recHitsInputLabel = cms.InputTag('gemRecHits'),
  idxFirstStrip = cms.int32(0),
  ClusterSizeBinNum = cms.int32(9),
  global_x_bound_min = cms.double(-350),
  global_x_bound_max = cms.double(350),
  global_y_bound_min = cms.double(-260),
  global_y_bound_max = cms.double(260),
  logCategory = cms.untracked.string('GEMRecHitSource'),
  mightGet = cms.optional.untracked.vstring
)
