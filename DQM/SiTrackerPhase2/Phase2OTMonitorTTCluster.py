import FWCore.ParameterSet.Config as cms

def Phase2OTMonitorTTCluster(**kwargs):
  mod = cms.EDProducer('Phase2OTMonitorTTCluster',
    TH1TTCluster_Barrel = cms.PSet(
      Nbinsx = cms.int32(7),
      xmax = cms.double(7.5),
      xmin = cms.double(0.5)
    ),
    TH1TTCluster_ECDiscs = cms.PSet(
      Nbinsx = cms.int32(6),
      xmax = cms.double(6.5),
      xmin = cms.double(0.5)
    ),
    TH1TTCluster_ECRings = cms.PSet(
      Nbinsx = cms.int32(16),
      xmin = cms.double(0.5),
      xmax = cms.double(16.5)
    ),
    TH1TTCluster_Eta = cms.PSet(
      Nbinsx = cms.int32(45),
      xmax = cms.double(5),
      xmin = cms.double(-5)
    ),
    TH1TTCluster_Phi = cms.PSet(
      Nbinsx = cms.int32(60),
      xmax = cms.double(3.5),
      xmin = cms.double(-3.5)
    ),
    TH1TTCluster_R = cms.PSet(
      Nbinsx = cms.int32(45),
      xmax = cms.double(120),
      xmin = cms.double(0)
    ),
    TH2TTCluster_Width = cms.PSet(
      Nbinsx = cms.int32(7),
      xmax = cms.double(6.5),
      xmin = cms.double(-0.5),
      Nbinsy = cms.int32(2),
      ymax = cms.double(1.5),
      ymin = cms.double(-0.5)
    ),
    TH2TTCluster_Position = cms.PSet(
      Nbinsx = cms.int32(960),
      xmax = cms.double(120),
      xmin = cms.double(-120),
      Nbinsy = cms.int32(960),
      ymax = cms.double(120),
      ymin = cms.double(-120)
    ),
    TH2TTCluster_RZ = cms.PSet(
      Nbinsx = cms.int32(900),
      xmax = cms.double(300),
      xmin = cms.double(-300),
      Nbinsy = cms.int32(900),
      ymax = cms.double(120),
      ymin = cms.double(0)
    ),
    TopFolderName = cms.string('TrackerPhase2TTCluster'),
    TTClusters = cms.InputTag('TTClustersFromPhase2TrackerDigis', 'ClusterInclusive'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
