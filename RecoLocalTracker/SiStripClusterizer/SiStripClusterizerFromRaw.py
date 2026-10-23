import FWCore.ParameterSet.Config as cms

def SiStripClusterizerFromRaw(*args, **kwargs):
  mod = cms.EDProducer('SiStripClusterizerFromRaw',
    ProductLabel = cms.InputTag('rawDataCollector'),
    ConditionsLabel = cms.string(''),
    onDemand = cms.bool(True),
    DoAPVEmulatorCheck = cms.bool(True),
    LegacyUnpacker = cms.bool(False),
    HybridZeroSuppressed = cms.bool(False),
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
    Algorithms = cms.PSet(
      CommonModeNoiseSubtractionMode = cms.string('Median'),
      useCMMeanMap = cms.bool(False),
      TruncateInSuppressor = cms.bool(True),
      doAPVRestore = cms.bool(False),
      SiStripFedZeroSuppressionMode = cms.uint32(4),
      PedestalSubtractionFedMode = cms.bool(True),
      Use10bitsTruncation = cms.bool(False),
      Percentile = cms.double(25),
      CutToAvoidSignal = cms.double(2),
      Iterations = cms.int32(3),
      ForceNoRestore = cms.bool(False),
      APVInspectMode = cms.string('BaselineFollower'),
      APVRestoreMode = cms.string(''),
      useRealMeanCM = cms.bool(False),
      MeanCM = cms.int32(0),
      DeltaCMThreshold = cms.uint32(20),
      Fraction = cms.double(0.2),
      Deviation = cms.uint32(25),
      restoreThreshold = cms.double(0.5),
      nSaturatedStrip = cms.uint32(2),
      nSigmaNoiseDerTh = cms.uint32(4),
      consecThreshold = cms.uint32(5),
      nSmooth = cms.uint32(9),
      distortionThreshold = cms.uint32(20),
      ApplyBaselineCleaner = cms.bool(True),
      CleaningSequence = cms.uint32(1),
      slopeX = cms.int32(3),
      slopeY = cms.int32(4),
      hitStripThreshold = cms.uint32(40),
      minStripsToFit = cms.uint32(4),
      ApplyBaselineRejection = cms.bool(True),
      filteredBaselineMax = cms.double(6),
      filteredBaselineDerivativeSumSquare = cms.double(30),
      discontinuityThreshold = cms.int32(12),
      lastGradient = cms.int32(10),
      sizeWindow = cms.int32(1),
      widthCluster = cms.int32(64)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
