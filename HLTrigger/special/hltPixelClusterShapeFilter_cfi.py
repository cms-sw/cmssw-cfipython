import FWCore.ParameterSet.Config as cms

hltPixelClusterShapeFilter = cms.EDFilter('HLTPixelClusterShapeFilter',
  saveTags = cms.bool(True),
  inputTag = cms.InputTag('hltSiPixelRecHits'),
  minZ = cms.double(-20),
  maxZ = cms.double(20.05),
  zStep = cms.double(0.2),
  clusterPars = cms.vdouble(
    0,
    0.0045
  ),
  nhitsTrunc = cms.int32(150),
  clusterTrunc = cms.double(2)
)
