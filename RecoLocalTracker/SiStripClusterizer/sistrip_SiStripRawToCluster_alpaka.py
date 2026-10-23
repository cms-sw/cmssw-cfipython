import FWCore.ParameterSet.Config as cms

def sistrip_SiStripRawToCluster_alpaka(*args, **kwargs):
  mod = cms.EDProducer('sistrip::SiStripRawToCluster@alpaka',
    ProductLabel = cms.InputTag('rawDataCollector'),
    ConditionsLabel = cms.string(''),
    CablingConditionsLabel = cms.string(''),
    DoAPVEmulatorCheck = cms.bool(False),
    Clusterizer = cms.PSet(
      Algorithm = cms.string('ThreeThresholdAlgorithm'),
      ConditionsLabel = cms.string(''),
      ChannelThreshold = cms.double(2),
      SeedThreshold = cms.double(3),
      ClusterThreshold = cms.double(5),
      MaxSequentialHoles = cms.uint32(0),
      MaxSequentialBad = cms.uint32(1),
      MaxAdjacentBad = cms.uint32(0),
      MaxClusterSize = cms.uint32(768),
      RemoveApvShots = cms.bool(True),
      setDetId = cms.bool(True),
      clusterChargeCut = cms.PSet(
        value = cms.double(-1)
      ),
      MaxSeedStrips = cms.uint32(200000)
    ),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string(''),
      synchronize = cms.optional.untracked.bool
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
