import FWCore.ParameterSet.Config as cms

GEMDQMSource = cms.EDProducer('GEMDQMSource',
  recHitsInputLabel = cms.InputTag('gemRecHits'),
  idxFirstStrip = cms.int32(0),
  global_x_bound_min = cms.double(-350),
  global_x_bound_max = cms.double(350),
  global_y_bound_min = cms.double(-260),
  global_y_bound_max = cms.double(260),
  mightGet = cms.optional.untracked.vstring
)
