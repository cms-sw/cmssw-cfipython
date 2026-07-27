import FWCore.ParameterSet.Config as cms

def Phase2OTMonitorTTCluster(*args, **kwargs):
  mod = cms.EDProducer('Phase2OTMonitorTTCluster',
    Num_L1Clusters_IMem_Barrel = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_IMem_Barrel'),
      title = cms.string('Num_L1Clusters_IMem_Barrel;Barrel Layer;# L1 Clusters'),
      NxBins = cms.int32(7),
      xmin = cms.double(0.5),
      xmax = cms.double(7.5)
    ),
    Num_L1Clusters_OMem_Barrel = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_OMem_Barrel'),
      title = cms.string('Num_L1Clusters_OMem_Barrel;Barrel Layer;# L1 Clusters'),
      NxBins = cms.int32(7),
      xmin = cms.double(0.5),
      xmax = cms.double(7.5)
    ),
    Num_L1Clusters_IMem_Endcap_Disc = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_IMem_Endcap_Disc'),
      title = cms.string('Num_L1Clusters_IMem_Endcap_Disc;Endcap Disc;# L1 Clusters'),
      NxBins = cms.int32(6),
      xmin = cms.double(0.5),
      xmax = cms.double(6.5)
    ),
    Num_L1Clusters_OMem_Endcap_Disc = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_OMem_Endcap_Disc'),
      title = cms.string('Num_L1Clusters_OMem_Endcap_Disc;Endcap Disc;# L1 Clusters'),
      NxBins = cms.int32(6),
      xmin = cms.double(0.5),
      xmax = cms.double(6.5)
    ),
    Num_L1Clusters_IMem_Endcap_Ring = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_IMem_Endcap_Ring'),
      title = cms.string('Num_L1Clusters_IMem_Endcap_Ring;Endcap Ring;# L1 Clusters'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Clusters_OMem_Endcap_Ring = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_OMem_Endcap_Ring'),
      title = cms.string('Num_L1Clusters_OMem_Endcap_Ring;Endcap Ring;# L1 Clusters'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Clusters_IMem_Disc_Fw_1 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_IMem_Disc+1'),
      title = cms.string('Num_L1Clusters_IMem_Disc+1;Endcap Ring;# L1 Clusters'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Clusters_IMem_Disc_Bw_1 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_IMem_Disc-1'),
      title = cms.string('Num_L1Clusters_IMem_Disc-1;Endcap Ring;# L1 Clusters'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Clusters_OMem_Disc_Fw_1 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_OMem_Disc+1'),
      title = cms.string('Num_L1Clusters_OMem_Disc+1;Endcap Ring;# L1 Clusters'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Clusters_OMem_Disc_Bw_1 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_OMem_Disc-1'),
      title = cms.string('Num_L1Clusters_OMem_Disc-1;Endcap Ring;# L1 Clusters'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Clusters_IMem_Disc_Fw_2 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_IMem_Disc+2'),
      title = cms.string('Num_L1Clusters_IMem_Disc+2;Endcap Ring;# L1 Clusters'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Clusters_IMem_Disc_Bw_2 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_IMem_Disc-2'),
      title = cms.string('Num_L1Clusters_IMem_Disc-2;Endcap Ring;# L1 Clusters'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Clusters_OMem_Disc_Fw_2 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_OMem_Disc+2'),
      title = cms.string('Num_L1Clusters_OMem_Disc+2;Endcap Ring;# L1 Clusters'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Clusters_OMem_Disc_Bw_2 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_OMem_Disc-2'),
      title = cms.string('Num_L1Clusters_OMem_Disc-2;Endcap Ring;# L1 Clusters'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Clusters_IMem_Disc_Fw_3 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_IMem_Disc+3'),
      title = cms.string('Num_L1Clusters_IMem_Disc+3;Endcap Ring;# L1 Clusters'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Clusters_IMem_Disc_Bw_3 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_IMem_Disc-3'),
      title = cms.string('Num_L1Clusters_IMem_Disc-3;Endcap Ring;# L1 Clusters'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Clusters_OMem_Disc_Fw_3 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_OMem_Disc+3'),
      title = cms.string('Num_L1Clusters_OMem_Disc+3;Endcap Ring;# L1 Clusters'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Clusters_OMem_Disc_Bw_3 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_OMem_Disc-3'),
      title = cms.string('Num_L1Clusters_OMem_Disc-3;Endcap Ring;# L1 Clusters'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Clusters_IMem_Disc_Fw_4 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_IMem_Disc+4'),
      title = cms.string('Num_L1Clusters_IMem_Disc+4;Endcap Ring;# L1 Clusters'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Clusters_IMem_Disc_Bw_4 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_IMem_Disc-4'),
      title = cms.string('Num_L1Clusters_IMem_Disc-4;Endcap Ring;# L1 Clusters'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Clusters_OMem_Disc_Fw_4 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_OMem_Disc+4'),
      title = cms.string('Num_L1Clusters_OMem_Disc+4;Endcap Ring;# L1 Clusters'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Clusters_OMem_Disc_Bw_4 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_OMem_Disc-4'),
      title = cms.string('Num_L1Clusters_OMem_Disc-4;Endcap Ring;# L1 Clusters'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Clusters_IMem_Disc_Fw_5 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_IMem_Disc+5'),
      title = cms.string('Num_L1Clusters_IMem_Disc+5;Endcap Ring;# L1 Clusters'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Clusters_IMem_Disc_Bw_5 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_IMem_Disc-5'),
      title = cms.string('Num_L1Clusters_IMem_Disc-5;Endcap Ring;# L1 Clusters'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Clusters_OMem_Disc_Fw_5 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_OMem_Disc+5'),
      title = cms.string('Num_L1Clusters_OMem_Disc+5;Endcap Ring;# L1 Clusters'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    Num_L1Clusters_OMem_Disc_Bw_5 = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('Num_L1Clusters_OMem_Disc-5'),
      title = cms.string('Num_L1Clusters_OMem_Disc-5;Endcap Ring;# L1 Clusters'),
      NxBins = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    L1Cluster_W = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Cluster_W'),
      title = cms.string('L1Cluster_W;L1 Cluster Width;Stack Member'),
      NxBins = cms.int32(7),
      xmin = cms.double(-0.5),
      xmax = cms.double(6.5),
      NyBins = cms.int32(2),
      ymin = cms.double(-0.5),
      ymax = cms.double(1.5)
    ),
    L1Cluster_Eta = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Cluster_Eta'),
      title = cms.string('L1Cluster_Eta;#eta;# L1 Clusters'),
      NxBins = cms.int32(45),
      xmin = cms.double(-5),
      xmax = cms.double(5)
    ),
    L1Cluster_Phi = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Cluster_Phi'),
      title = cms.string('L1Cluster_Phi;#phi;# L1 Clusters'),
      NxBins = cms.int32(60),
      xmin = cms.double(-3.5),
      xmax = cms.double(3.5)
    ),
    L1Cluster_R = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Cluster_R'),
      title = cms.string('L1Cluster_R;R [cm];# L1 Clusters'),
      NxBins = cms.int32(45),
      xmin = cms.double(0),
      xmax = cms.double(120)
    ),
    L1Cluster_Global_Position_Barrel_XY = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Cluster_Global_Position_Barrel_XY'),
      title = cms.string('L1Cluster_Global_Position_Barrel_XY;L1 Cluster Barrel position x [cm];L1 Cluster Barrel position y [cm]'),
      NxBins = cms.int32(960),
      xmin = cms.double(-120),
      xmax = cms.double(120),
      NyBins = cms.int32(960),
      ymin = cms.double(-120),
      ymax = cms.double(120)
    ),
    L1Cluster_Global_Position_Endcap_Fw_XY = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Cluster_Global_Position_Endcap_Fw_XY'),
      title = cms.string('L1Cluster_Global_Position_Endcap_Fw_XY;L1 Cluster Forward Endcap position x [cm];L1 Cluster Forward Endcap position y [cm]'),
      NxBins = cms.int32(960),
      xmin = cms.double(-120),
      xmax = cms.double(120),
      NyBins = cms.int32(960),
      ymin = cms.double(-120),
      ymax = cms.double(120)
    ),
    L1Cluster_Global_Position_Endcap_Bw_XY = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Cluster_Global_Position_Endcap_Bw_XY'),
      title = cms.string('L1Cluster_Global_Position_Endcap_Bw_XY;L1 Cluster Backward Endcap position x [cm];L1 Cluster Backward Endcap position y [cm]'),
      NxBins = cms.int32(960),
      xmin = cms.double(-120),
      xmax = cms.double(120),
      NyBins = cms.int32(960),
      ymin = cms.double(-120),
      ymax = cms.double(120)
    ),
    L1Cluster_Global_Position_RZ = cms.PSet(
      switch = cms.bool(True),
      name = cms.string('L1Cluster_Global_Position_RZ'),
      title = cms.string('L1Cluster_Global_Position_RZ;L1 Cluster position z [cm];L1 Cluster position #rho [cm]'),
      NxBins = cms.int32(900),
      xmin = cms.double(-300),
      xmax = cms.double(300),
      NyBins = cms.int32(900),
      ymin = cms.double(0),
      ymax = cms.double(120)
    ),
    TopFolderName = cms.string('OuterTracker'),
    TTClusters = cms.InputTag('TTClustersFromPhase2TrackerDigis', 'ClusterInclusive'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
