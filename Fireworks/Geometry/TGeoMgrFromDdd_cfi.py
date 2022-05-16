import FWCore.ParameterSet.Config as cms

TGeoMgrFromDdd = cms.ESProducer('TGeoMgrFromDdd',
  level = cms.untracked.int32(10),
  verbose = cms.untracked.bool(False),
  fullName = cms.untracked.bool(True),
  appendToDataLabel = cms.string('')
)
