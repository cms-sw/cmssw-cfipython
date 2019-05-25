import FWCore.ParameterSet.Config as cms

templates2 = cms.ESProducer('PixelCPEClusterRepairESProducer',
  DoLorentz = cms.bool(True),
  DoCosmics = cms.bool(False),
  LoadTemplatesFromDB = cms.bool(True),
  RunDamagedClusters = cms.bool(False),
  ComponentName = cms.string('PixelCPEClusterRepair'),
  MinChargeRatio = cms.double(0.8),
  MaxSizeMismatchInY = cms.double(0.3),
  Alpha2Order = cms.bool(True),
  Recommend2D = cms.vstring(
    'PXB 2',
    'PXB 3',
    'PXB 4'
  ),
  ClusterProbComputationFlag = cms.int32(0),
  speed = cms.int32(-2),
  UseClusterSplitter = cms.bool(False),
  appendToDataLabel = cms.string('')
)
