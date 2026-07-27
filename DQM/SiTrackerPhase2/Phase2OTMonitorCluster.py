import FWCore.ParameterSet.Config as cms

def Phase2OTMonitorCluster(*args, **kwargs):
  mod = cms.EDProducer('Phase2OTMonitorCluster',
    GlobalNClusters = cms.PSet(
      name = cms.string('Num_Clusters'),
      title = cms.string('Number of clusters;Number of clusters per event;'),
      xmin = cms.double(0),
      switch = cms.bool(True),
      xmax = cms.double(350000),
      NxBins = cms.int32(150)
    ),
    CrackOverview = cms.PSet(
      name = cms.string('Crack_Overview_OTcluster'),
      title = cms.string('Crack_Overview_clusters;Module;Layer'),
      xmin = cms.double(0),
      switch = cms.bool(False),
      xmax = cms.double(13),
      ymin = cms.double(0),
      ymax = cms.double(7.5)
    ),
    GlobalPositionXY_P = cms.PSet(
      name = cms.string('Cluster_Global_Position_XY_P'),
      title = cms.string('Cluster Position XY P;Cluster position x [cm];Cluster position y [cm];'),
      NxBins = cms.int32(1250),
      xmin = cms.double(-125),
      xmax = cms.double(125),
      NyBins = cms.int32(1250),
      ymin = cms.double(-125),
      ymax = cms.double(125),
      switch = cms.bool(True)
    ),
    GlobalPositionXY_S = cms.PSet(
      name = cms.string('Cluster_Global_Position_XY_S'),
      title = cms.string('Cluster Position XY S;Cluster position x [cm];Cluster position y [cm];'),
      NxBins = cms.int32(1250),
      xmin = cms.double(-125),
      xmax = cms.double(125),
      NyBins = cms.int32(1250),
      ymin = cms.double(-125),
      ymax = cms.double(125),
      switch = cms.bool(True)
    ),
    GlobalPositionRZ_P = cms.PSet(
      name = cms.string('Cluster_Global_Position_RZ_P'),
      title = cms.string('Cluster Position RZ P;Cluster position z [cm];Cluster position #rho [cm]'),
      NxBins = cms.int32(1500),
      xmin = cms.double(-300),
      xmax = cms.double(300),
      NyBins = cms.int32(1250),
      ymin = cms.double(0),
      ymax = cms.double(125),
      switch = cms.bool(True)
    ),
    GlobalPositionRZ_S = cms.PSet(
      name = cms.string('Cluster_Global_Position_RZ_S'),
      title = cms.string('Cluster Position RZ S;Cluster position z [cm];Cluster position #rho [cm]'),
      NxBins = cms.int32(1500),
      xmin = cms.double(-300),
      xmax = cms.double(300),
      NyBins = cms.int32(1250),
      ymin = cms.double(0),
      ymax = cms.double(125),
      switch = cms.bool(True)
    ),
    NClusters_Barrel = cms.PSet(
      name = cms.string('Num_Clusters_Barrel'),
      title = cms.string('Number of clusters per Barrel Layer;Barrel Layer;Number of clusters'),
      NxBins = cms.int32(7),
      xmin = cms.double(0.5),
      xmax = cms.double(7.5),
      switch = cms.bool(True)
    ),
    NClustersLayer_P = cms.PSet(
      name = cms.string('Num_Clusters_Layer_P'),
      title = cms.string('Number Of Clusters P Layer;Number of clusters per event (macro pixel sensor);'),
      xmin = cms.double(0),
      xmax = cms.double(28000),
      NxBins = cms.int32(150),
      switch = cms.bool(True)
    ),
    NClustersLayer_S = cms.PSet(
      name = cms.string('Num_Clusters_Layer_S'),
      title = cms.string('Number Of Clusters S Layer;Number of clusters per event (strip sensor);'),
      xmin = cms.double(0),
      xmax = cms.double(28000),
      NxBins = cms.int32(150),
      switch = cms.bool(True)
    ),
    ClusterSize_P = cms.PSet(
      name = cms.string('Cluster_Size_P'),
      title = cms.string('Cluster Size P;Cluster size (macro pixel sensor);'),
      xmin = cms.double(-0.5),
      xmax = cms.double(30.5),
      NxBins = cms.int32(31),
      switch = cms.bool(True)
    ),
    ClusterSize_S = cms.PSet(
      name = cms.string('Cluster_Size_S'),
      title = cms.string('Cluster Size S;Cluster size (strip sensor);'),
      xmin = cms.double(-0.5),
      xmax = cms.double(30.5),
      NxBins = cms.int32(31),
      switch = cms.bool(True)
    ),
    GlobalPositionXY_perlayer_P = cms.PSet(
      name = cms.string('Cluster_Position_XY_perLayer_P'),
      title = cms.string('Cluster Position XY per Layer P;Cluster position x [cm];Cluster position y [cm];'),
      NxBins = cms.int32(1250),
      xmin = cms.double(-125),
      xmax = cms.double(125),
      NyBins = cms.int32(1250),
      ymin = cms.double(-125),
      ymax = cms.double(125),
      switch = cms.bool(False)
    ),
    GlobalPositionXY_perlayer_S = cms.PSet(
      name = cms.string('Cluster_Position_XY_perLayer_S'),
      title = cms.string('Cluster Position XY per Layer S;Cluster position x [cm];Cluster position y [cm];'),
      NxBins = cms.int32(1250),
      xmin = cms.double(-125),
      xmax = cms.double(125),
      NyBins = cms.int32(1250),
      ymin = cms.double(-125),
      ymax = cms.double(125),
      switch = cms.bool(False)
    ),
    PositionOfClusters_2S = cms.PSet(
      name = cms.string('Position_Clusters_2S_module'),
      title = cms.string('Positions Of Clusters 2S_module;Strip;Half-module;'),
      NxBins = cms.int32(1016),
      xmin = cms.double(0.5),
      xmax = cms.double(1016.5),
      NyBins = cms.int32(5),
      ymin = cms.double(-2.5),
      ymax = cms.double(2.5),
      switch = cms.bool(False)
    ),
    PositionOfClusters_2SLadder = cms.PSet(
      name = cms.string('Position_Clusters_2S_Ladder'),
      title = cms.string('Positions Of Clusters 2S_Ladder;Module;Half-module;'),
      NxBins = cms.int32(25),
      xmin = cms.double(-12.5),
      xmax = cms.double(12.5),
      NyBins = cms.int32(5),
      ymin = cms.double(-2.5),
      ymax = cms.double(2.5),
      switch = cms.bool(True)
    ),
    TopFolderName = cms.string('OuterTracker'),
    clusterSrc = cms.InputTag('siPhase2Clusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
