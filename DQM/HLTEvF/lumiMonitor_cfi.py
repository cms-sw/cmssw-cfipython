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
    pixelClusterPSet = cms.PSet(
      nbins = cms.required.int32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    lumiPSet = cms.PSet(
      nbins = cms.required.int32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    puPSet = cms.PSet(
      nbins = cms.required.int32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    pixellumiPSet = cms.PSet(
      nbins = cms.required.int32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    lsPSet = cms.PSet(
      nbins = cms.int32(2500)
    )
  ),
  mightGet = cms.optional.untracked.vstring
)
