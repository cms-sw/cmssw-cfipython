import FWCore.ParameterSet.Config as cms

def SiStripClusterizerFromRawGPU(**kwargs):
  mod = cms.EDProducer('SiStripClusterizerFromRawGPU',
    ProductLabel = cms.InputTag('rawDataCollector'),
    ConditionsLabel = cms.string(''),
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
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
