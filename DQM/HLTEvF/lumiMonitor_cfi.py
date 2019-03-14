import FWCore.ParameterSet.Config as cms

lumiMonitor = cms.EDAnalyzer('LumiMonitor',
  pixelClusters = cms.InputTag('hltSiPixelClusters'),
  scalers = cms.InputTag('hltScalersRawToDigi'),
  FolderName = cms.string('HLT/LumiMonitoring'),
  doPixelLumi = cms.bool(False),
  useBPixLayer1 = cms.bool(False),
  minNumberOfPixelsPerCluster = cms.int32(2),
  minPixelClusterCharge = cms.double(15000),
  histoPSet = cms.PSet(
    pixelClusterPSet = cms.PSet(),
    lumiPSet = cms.PSet(),
    pixellumiPSet = cms.PSet(),
    lsPSet = cms.PSet(
      nbins = cms.int32(2500)
    )
  )
)
