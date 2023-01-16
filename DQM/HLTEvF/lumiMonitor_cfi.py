import FWCore.ParameterSet.Config as cms

lumiMonitor = cms.EDProducer('LumiMonitor',
  pixelClusters = cms.InputTag('hltSiPixelClusters'),
  scalers = cms.InputTag('hltScalersRawToDigi'),
  onlineMetaDataDigis = cms.InputTag('hltOnlineMetaDataDigis'),
  folderName = cms.string('HLT/LumiMonitoring'),
  doPixelLumi = cms.bool(False),
  useBPixLayer1 = cms.bool(False),
  minNumberOfPixelsPerCluster = cms.int32(2),
  minPixelClusterCharge = cms.double(15000),
  histoPSet = cms.PSet(
    lsPSet = cms.PSet(
      nbins = cms.int32(2500)
    ),
    puPSet = cms.PSet(
      nbins = cms.int32(130),
      xmin = cms.double(0),
      xmax = cms.double(130)
    ),
    lumiPSet = cms.PSet(
      nbins = cms.int32(5000),
      xmin = cms.double(0),
      xmax = cms.double(20000)
    ),
    pixellumiPSet = cms.PSet(
      nbins = cms.int32(300),
      xmin = cms.double(0),
      xmax = cms.double(3)
    ),
    pixelClusterPSet = cms.PSet(
      nbins = cms.int32(200),
      xmin = cms.double(-0.5),
      xmax = cms.double(19999.5)
    )
  ),
  mightGet = cms.optional.untracked.vstring
)
