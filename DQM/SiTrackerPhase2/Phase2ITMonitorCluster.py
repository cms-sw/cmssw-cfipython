import FWCore.ParameterSet.Config as cms

def Phase2ITMonitorCluster(*args, **kwargs):
  mod = cms.EDProducer('Phase2ITMonitorCluster',
    GlobalPositionRZ_PXB = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Clusters_Global_Position_RZ_IT_barrel'),
      title = cms.string('Clusters_Global_Position_RZ_IT_barrel;z [mm];r [mm]'),
      NxBins = cms.int32(1500),
      xmin = cms.double(-3000),
      xmax = cms.double(3000),
      NyBins = cms.int32(300),
      ymin = cms.double(0),
      ymax = cms.double(300)
    ),
    GlobalPositionXY_PXB = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Clusters_Global_Position_XY_IT_barrel'),
      title = cms.string('Clusters_Global_Position_XY_IT_barrel;x [mm];y [mm]'),
      NxBins = cms.int32(600),
      xmin = cms.double(-300),
      xmax = cms.double(300),
      NyBins = cms.int32(600),
      ymin = cms.double(-300),
      ymax = cms.double(300)
    ),
    GlobalPositionRZ_PXEC = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Clusters_Global_Position_RZ_IT_endcap'),
      title = cms.string('Clusters_Global_Position_RZ_IT_endcap;z [mm];r [mm]'),
      NxBins = cms.int32(1500),
      xmin = cms.double(-3000),
      xmax = cms.double(3000),
      NyBins = cms.int32(300),
      ymin = cms.double(0),
      ymax = cms.double(300)
    ),
    GlobalPositionXY_PXEC = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Clusters_Global_Position_XY_IT_endcap'),
      title = cms.string('Clusters_Global_Position_XY_IT_endcap;x [mm];y [mm]'),
      NxBins = cms.int32(600),
      xmin = cms.double(-300),
      xmax = cms.double(300),
      NyBins = cms.int32(600),
      ymin = cms.double(-300),
      ymax = cms.double(300)
    ),
    NClustersLayer = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_Clusters_Per_Event'),
      title = cms.string('Number Of Clusters per event in {};Number of Clusters per event;Number of events'),
      NxBins = cms.int32(150),
      xmin = cms.double(0),
      xmax = cms.double(250000)
    ),
    ClusterCharge = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Cluster_Charge'),
      title = cms.string('Cluster charge in {};Cluster charge;Number of clusters'),
      NxBins = cms.int32(100),
      xmin = cms.double(0),
      xmax = cms.double(100000)
    ),
    ClusterSize = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Cluster_Size'),
      title = cms.string('Cluster size in {};Cluster size;Number of clusters'),
      NxBins = cms.int32(31),
      xmin = cms.double(-0.5),
      xmax = cms.double(30.5)
    ),
    ClusterSizeY = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Cluster_Size_Y'),
      title = cms.string('Cluster size Y in {};Cluster size Y;Number of clusters'),
      NxBins = cms.int32(31),
      xmin = cms.double(-0.5),
      xmax = cms.double(30.5)
    ),
    ClusterSizeX = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Cluster_Size_X'),
      title = cms.string('Cluster size X in {};Cluster size X;Number of clusters'),
      NxBins = cms.int32(31),
      xmin = cms.double(-0.5),
      xmax = cms.double(30.5)
    ),
    XY_byWheel_EPix = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Cluster_XY_Wheel_'),
      title = cms.string('XY position of clusters in {} wheel ;x [mm];y [mm]'),
      NxBins = cms.int32(300),
      xmin = cms.double(-300),
      xmax = cms.double(300),
      NyBins = cms.int32(300),
      ymin = cms.double(-300),
      ymax = cms.double(300)
    ),
    XY_byWheel_FPix = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Cluster_XY_Wheel_'),
      title = cms.string('XY position of clusters in {} wheel ;x [mm];y [mm]'),
      NxBins = cms.int32(200),
      xmin = cms.double(-200),
      xmax = cms.double(200),
      NyBins = cms.int32(200),
      ymin = cms.double(-200),
      ymax = cms.double(200)
    ),
    Pos_Signed_Modules_and_Ladders = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_Clusters_Modules_Ladders'),
      title = cms.string('Number of Clusters by Module and Ladder number in {};Signed Module;Signed Ladder'),
      NxBins = cms.int32(11),
      xmin = cms.double(-5.5),
      xmax = cms.double(5.5),
      NyBins = cms.int32(2),
      ymin = cms.double(0.5),
      ymax = cms.double(2.5)
    ),
    TopFolderName = cms.string('InnerTracker'),
    ReducedOutput = cms.bool(False),
    InnerPixelClusterSource = cms.InputTag('siPixelClusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
