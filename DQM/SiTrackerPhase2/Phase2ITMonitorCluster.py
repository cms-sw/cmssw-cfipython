import FWCore.ParameterSet.Config as cms

def Phase2ITMonitorCluster(*args, **kwargs):
  mod = cms.EDProducer('Phase2ITMonitorCluster',
    GlobalNClusters = cms.PSet(
      name = cms.string('Num_Clusters'),
      title = cms.string('NumberClusters;Number of Clusters;'),
      xmin = cms.double(0),
      switch = cms.bool(True),
      xmax = cms.double(300000),
      NxBins = cms.int32(150)
    ),
    GlobalPositionRZ_PXB = cms.PSet(
      name = cms.string('Clusters_Global_Position_RZ_IT_barrel'),
      title = cms.string('Clusters_Global_Position_RZ_IT_barrel;z [mm];r [mm]'),
      ymax = cms.double(300),
      NxBins = cms.int32(1500),
      NyBins = cms.int32(300),
      switch = cms.bool(True),
      xmax = cms.double(3000),
      xmin = cms.double(-3000),
      ymin = cms.double(0)
    ),
    GlobalPositionXY_PXB = cms.PSet(
      name = cms.string('Clusters_Global_Position_XY_IT_barrel'),
      title = cms.string('Clusters_Global_Position_XY_IT_barrel;x [mm];y [mm];'),
      ymax = cms.double(300),
      NxBins = cms.int32(600),
      NyBins = cms.int32(600),
      switch = cms.bool(True),
      xmax = cms.double(300),
      xmin = cms.double(-300),
      ymin = cms.double(-300)
    ),
    GlobalPositionRZ_PXEC = cms.PSet(
      name = cms.string('Clusters_Global_Position_RZ_IT_endcap'),
      title = cms.string('Clusters_Global_Position_RZ_IT_endcap;z [mm];r [mm]'),
      ymax = cms.double(300),
      NxBins = cms.int32(1500),
      NyBins = cms.int32(300),
      switch = cms.bool(True),
      xmax = cms.double(3000),
      xmin = cms.double(-3000),
      ymin = cms.double(0)
    ),
    GlobalPositionXY_PXEC = cms.PSet(
      name = cms.string('Clusters_Global_Position_XY_IT_endcap'),
      title = cms.string('Clusters_Global_Position_XY_IT_endcap; x [mm]; y [mm]'),
      ymax = cms.double(300),
      NxBins = cms.int32(600),
      NyBins = cms.int32(600),
      switch = cms.bool(True),
      xmax = cms.double(300),
      xmin = cms.double(-300),
      ymin = cms.double(-300)
    ),
    NClustersLayer = cms.PSet(
      name = cms.string('Num_Clusters_Layer'),
      title = cms.string('NumberOfClusters;Number of Clusters;'),
      xmin = cms.double(0),
      switch = cms.bool(True),
      xmax = cms.double(20000),
      NxBins = cms.int32(150)
    ),
    ClusterCharge = cms.PSet(
      name = cms.string('Cluster_Charge'),
      title = cms.string(';Cluster charge;'),
      xmin = cms.double(0),
      switch = cms.bool(True),
      xmax = cms.double(100000),
      NxBins = cms.int32(100)
    ),
    ClusterSize = cms.PSet(
      name = cms.string('Cluster_Size'),
      title = cms.string(';Cluster size;'),
      xmin = cms.double(-0.5),
      xmax = cms.double(30.5),
      NxBins = cms.int32(31),
      switch = cms.bool(True)
    ),
    ClusterSizeY = cms.PSet(
      name = cms.string('Cluster_Size_Y'),
      title = cms.string(';Cluster sizeY;'),
      xmin = cms.double(-0.5),
      switch = cms.bool(True),
      xmax = cms.double(30.5),
      NxBins = cms.int32(31)
    ),
    ClusterSizeX = cms.PSet(
      name = cms.string('Cluster_Size_X'),
      title = cms.string(';Cluster sizeX;'),
      xmin = cms.double(-0.5),
      switch = cms.bool(True),
      xmax = cms.double(30.5),
      NxBins = cms.int32(31)
    ),
    TopFolderName = cms.string('InnerTracker'),
    InnerPixelClusterSource = cms.InputTag('siPixelClusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
