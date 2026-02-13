import FWCore.ParameterSet.Config as cms

def Phase2OTMonitorCluster(*args, **kwargs):
  mod = cms.EDProducer('Phase2OTMonitorCluster',
    GlobalNClusters = cms.PSet(
      name = cms.string('NumberOfClusters'),
      title = cms.string(';Number of clusters per event;'),
      xmin = cms.double(0),
      switch = cms.bool(True),
      xmax = cms.double(350000),
      NxBins = cms.int32(150)
    ),
    GlobalPositionXY_P = cms.PSet(
      name = cms.string('Cluster_Position_XY_P'),
      title = cms.string('Cluster_Position_XY_P;Cluster position x [cm];Cluster position y [cm];'),
      NxBins = cms.int32(1250),
      xmin = cms.double(-125),
      xmax = cms.double(125),
      NyBins = cms.int32(1250),
      ymin = cms.double(-125),
      ymax = cms.double(125),
      switch = cms.bool(True)
    ),
    GlobalPositionXY_S = cms.PSet(
      name = cms.string('Cluster_Position_XY_S'),
      title = cms.string('Cluster_Position_XY_S;Cluster position x [cm];Cluster position y [cm];'),
      NxBins = cms.int32(1250),
      xmin = cms.double(-125),
      xmax = cms.double(125),
      NyBins = cms.int32(1250),
      ymin = cms.double(-125),
      ymax = cms.double(125),
      switch = cms.bool(True)
    ),
    GlobalPositionRZ_P = cms.PSet(
      name = cms.string('Cluster_Position_RZ_P'),
      title = cms.string('Cluster_Position_RZ_P;Cluster position z [cm];Cluster position #rho [cm]'),
      NxBins = cms.int32(1500),
      xmin = cms.double(-300),
      xmax = cms.double(300),
      NyBins = cms.int32(1250),
      ymin = cms.double(0),
      ymax = cms.double(125),
      switch = cms.bool(True)
    ),
    GlobalPositionRZ_S = cms.PSet(
      name = cms.string('Cluster_Position_RZ_S'),
      title = cms.string('Cluster_Position_RZ_S;Cluster position z [cm];Cluster position #rho [cm]'),
      NxBins = cms.int32(1500),
      xmin = cms.double(-300),
      xmax = cms.double(300),
      NyBins = cms.int32(1250),
      ymin = cms.double(0),
      ymax = cms.double(125),
      switch = cms.bool(True)
    ),
    NClusters_Barrel = cms.PSet(
      name = cms.string('NumberOfClusters_Barrel'),
      title = cms.string('Number of clusters per Barrel Layer;Barrel Layer;Number of clusters'),
      NxBins = cms.int32(7),
      xmin = cms.double(0.5),
      xmax = cms.double(7.5),
      switch = cms.bool(True)
    ),
    NClustersLayer_P = cms.PSet(
      name = cms.string('NumberOfClusters_Layer_P'),
      title = cms.string(';Number of clusters per event (macro pixel sensor);'),
      xmin = cms.double(0),
      xmax = cms.double(28000),
      NxBins = cms.int32(150),
      switch = cms.bool(True)
    ),
    NClustersLayer_S = cms.PSet(
      name = cms.string('NumberOfClusters_Layer_S'),
      title = cms.string(';Number of clusters per event (strip sensor);'),
      xmin = cms.double(0),
      xmax = cms.double(28000),
      NxBins = cms.int32(150),
      switch = cms.bool(True)
    ),
    ClusterSize_P = cms.PSet(
      name = cms.string('Cluster_Size_P'),
      title = cms.string(';Cluster size (macro pixel sensor);'),
      xmin = cms.double(-0.5),
      xmax = cms.double(30.5),
      NxBins = cms.int32(31),
      switch = cms.bool(True)
    ),
    ClusterSize_S = cms.PSet(
      name = cms.string('Cluster_Size_S'),
      title = cms.string(';Cluster size (strip sensor);'),
      xmin = cms.double(-0.5),
      xmax = cms.double(30.5),
      NxBins = cms.int32(31),
      switch = cms.bool(True)
    ),
    GlobalPositionXY_perlayer_P = cms.PSet(
      name = cms.string('Cluster_Position_XY_perLayer_P'),
      title = cms.string('Cluster_Position_XY_perLayer_P;Cluster position x [cm];Cluster position y [cm];'),
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
      title = cms.string('Cluster_Position_XY_perLayer_S;Cluster position x [cm];Cluster position y [cm];'),
      NxBins = cms.int32(1250),
      xmin = cms.double(-125),
      xmax = cms.double(125),
      NyBins = cms.int32(1250),
      ymin = cms.double(-125),
      ymax = cms.double(125),
      switch = cms.bool(False)
    ),
    LocalPositionXY_P = cms.PSet(
      name = cms.string('Cluster_Local_Position_XY_P'),
      title = cms.string('Cluster_Local_Position_XY_P;Cluster position x [cm];Cluster position y [cm];'),
      NxBins = cms.int32(25),
      xmin = cms.double(-5),
      xmax = cms.double(5),
      NyBins = cms.int32(15),
      ymin = cms.double(-3),
      ymax = cms.double(3),
      switch = cms.bool(True)
    ),
    LocalPositionXY_S = cms.PSet(
      name = cms.string('Cluster_Local_Position_XY_S'),
      title = cms.string('Cluster_Local_Position_XY_S;Cluster position x [cm];Cluster position y [cm];'),
      NxBins = cms.int32(25),
      xmin = cms.double(-5),
      xmax = cms.double(5),
      NyBins = cms.int32(15),
      ymin = cms.double(-3),
      ymax = cms.double(3),
      switch = cms.bool(True)
    ),
    PositionOfClusters_2S = cms.PSet(
      name = cms.string('PositionOfClusters_2S_module'),
      title = cms.string('PositionsOfClusters_2S_module;Strip;Half-module;'),
      NxBins = cms.int32(1016),
      xmin = cms.double(0.5),
      xmax = cms.double(1016.5),
      NyBins = cms.int32(5),
      ymin = cms.double(-2.5),
      ymax = cms.double(2.5),
      switch = cms.bool(False)
    ),
    PositionOfClusters_2SLadder = cms.PSet(
      name = cms.string('PositionOfClusters_2S_Ladder'),
      title = cms.string('PositionsOfClusters_2S_Ladder;Module;Half-module;'),
      NxBins = cms.int32(25),
      xmin = cms.double(-12.5),
      xmax = cms.double(12.5),
      NyBins = cms.int32(5),
      ymin = cms.double(-2.5),
      ymax = cms.double(2.5),
      switch = cms.bool(True)
    ),
    TopFolderName = cms.string('TrackerPhase2OTCluster'),
    clusterSrc = cms.InputTag('siPhase2Clusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
