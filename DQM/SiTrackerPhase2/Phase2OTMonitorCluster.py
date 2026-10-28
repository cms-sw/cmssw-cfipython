import FWCore.ParameterSet.Config as cms

def Phase2OTMonitorCluster(*args, **kwargs):
  mod = cms.EDProducer('Phase2OTMonitorCluster',
    CrackOverview = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Crack_Overview_OT_Cluster'),
      title = cms.string('Crack_Overview_OT_Clusters;Module;Layer'),
      NxBins = cms.int32(0),
      xmin = cms.double(0),
      xmax = cms.double(13),
      NyBins = cms.int32(0),
      ymin = cms.double(0),
      ymax = cms.double(7.5)
    ),
    PositionOfClusters_2S = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Position_Clusters_2S_module'),
      title = cms.string('Positions of clusters in 2S module;Strip;Half-module'),
      NxBins = cms.int32(1016),
      xmin = cms.double(0.5),
      xmax = cms.double(1016.5),
      NyBins = cms.int32(5),
      ymin = cms.double(-2.5),
      ymax = cms.double(2.5)
    ),
    NClusters_Barrel = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_Clusters_Barrel'),
      title = cms.string('Number of clusters per Barrel Layer;Barrel Layer;Number of clusters'),
      NxBins = cms.int32(6),
      xmin = cms.double(0.5),
      xmax = cms.double(6.5)
    ),
    GlobalPositionXY_P = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Cluster_Global_Position_XY_P'),
      title = cms.string('Cluster Position XY P;Cluster position x [cm];Cluster position y [cm]'),
      NxBins = cms.int32(1250),
      xmin = cms.double(-125),
      xmax = cms.double(125),
      NyBins = cms.int32(1250),
      ymin = cms.double(-125),
      ymax = cms.double(125)
    ),
    GlobalPositionXY_S = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Cluster_Global_Position_XY_S'),
      title = cms.string('Cluster Position XY S;Cluster position x [cm];Cluster position y [cm]'),
      NxBins = cms.int32(1250),
      xmin = cms.double(-125),
      xmax = cms.double(125),
      NyBins = cms.int32(1250),
      ymin = cms.double(-125),
      ymax = cms.double(125)
    ),
    GlobalPositionRZ_P = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Cluster_Global_Position_RZ_P'),
      title = cms.string('Cluster Position RZ P;Cluster position z [cm];Cluster position #rho [cm]'),
      NxBins = cms.int32(1500),
      xmin = cms.double(-300),
      xmax = cms.double(300),
      NyBins = cms.int32(1250),
      ymin = cms.double(0),
      ymax = cms.double(125)
    ),
    GlobalPositionRZ_S = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Cluster_Global_Position_RZ_S'),
      title = cms.string('Cluster Position RZ S;Cluster position z [cm];Cluster position #rho [cm]'),
      NxBins = cms.int32(1500),
      xmin = cms.double(-300),
      xmax = cms.double(300),
      NyBins = cms.int32(1250),
      ymin = cms.double(0),
      ymax = cms.double(125)
    ),
    NClustersLayer_P = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_Clusters_Per_Event_P'),
      title = cms.string('Number Of Clusters in Pixels in {};Number of clusters per event (macro pixel sensor);'),
      NxBins = cms.int32(150),
      xmin = cms.double(0),
      xmax = cms.double(300000)
    ),
    NClustersLayer_S = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_Clusters_Per_Event_S'),
      title = cms.string('Number Of Clusters in strips in {};Number of clusters per event (strip sensor);'),
      NxBins = cms.int32(150),
      xmin = cms.double(0),
      xmax = cms.double(300000)
    ),
    ClusterSize_P = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Cluster_Size_P'),
      title = cms.string('Cluster Size in Pixels in {};Cluster size (macro pixel sensor);'),
      NxBins = cms.int32(31),
      xmin = cms.double(-0.5),
      xmax = cms.double(30.5)
    ),
    ClusterSize_S = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Cluster_Size_S'),
      title = cms.string('Cluster Size in strips in {};Cluster size (strip sensor);'),
      NxBins = cms.int32(31),
      xmin = cms.double(-0.5),
      xmax = cms.double(30.5)
    ),
    PositionOfClusters_2SLadder = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Position_Clusters_2S_Ladder'),
      title = cms.string(';;'),
      NxBins = cms.int32(25),
      xmin = cms.double(-12.5),
      xmax = cms.double(12.5),
      NyBins = cms.int32(5),
      ymin = cms.double(-2.5),
      ymax = cms.double(2.5)
    ),
    TopFolderName = cms.string('OuterTracker'),
    ReducedOutput = cms.bool(False),
    clusterSrc = cms.InputTag('siPhase2Clusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
