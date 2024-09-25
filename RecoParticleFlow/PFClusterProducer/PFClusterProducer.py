import FWCore.ParameterSet.Config as cms

def PFClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('PFClusterProducer',
    recHitsSource = cms.InputTag(''),
    usePFThresholdsFromDB = cms.bool(False),
    recHitCleaners = cms.VPSet(
    ),
    seedCleaners = cms.VPSet(
    ),
    seedFinder = cms.PSet(
      algoName = cms.string(''),
      nNeighbours = cms.int32(0),
      thresholdsByDetector = cms.VPSet(
      )
    ),
    initialClusteringStep = cms.PSet(
      algoName = cms.string(''),
      thresholdsByDetector = cms.VPSet(
      ),
      useCornerCells = cms.bool(False),
      clusterSrc = cms.InputTag(''),
      filterByTracksterIteration = cms.bool(False),
      filterByTracksterPID = cms.bool(False),
      filter_on_categories = cms.vint32(),
      filter_on_iterations = cms.vint32(),
      pid_threshold = cms.double(0),
      tracksterSrc = cms.InputTag(''),
      exclusiveFraction = cms.double(0),
      invisibleFraction = cms.double(0),
      maxDistanceFilter = cms.bool(False),
      maxDistance = cms.double(0),
      maxDforTimingSquared = cms.double(0),
      timeOffset = cms.double(0),
      minNHitsforTiming = cms.uint32(0),
      useMCFractionsForExclEnergy = cms.bool(False),
      hadronCalib = cms.vdouble(),
      egammaCalib = cms.vdouble(),
      calibMinEta = cms.double(0),
      calibMaxEta = cms.double(0),
      simClusterSrc = cms.InputTag('')
    ),
    pfClusterBuilder = cms.PSet(
      algoName = cms.string(''),
      allCellsPositionCalc = cms.PSet(
        algoName = cms.string(''),
        minFractionInCalc = cms.double(0),
        posCalcNCrystals = cms.int32(-1),
        logWeightDenominatorByDetector = cms.VPSet(
        ),
        logWeightDenominator = cms.double(0),
        minAllowedNormalization = cms.double(0),
        timeResolutionCalcBarrel = cms.PSet(
          constantTerm = cms.double(0),
          constantTermLowE = cms.double(0),
          corrTermLowE = cms.double(0),
          noiseTerm = cms.double(0),
          noiseTermLowE = cms.double(0),
          threshHighE = cms.double(-1),
          threshLowE = cms.double(-1)
        ),
        timeResolutionCalcEndcap = cms.PSet(
          constantTerm = cms.double(0),
          constantTermLowE = cms.double(0),
          corrTermLowE = cms.double(0),
          noiseTerm = cms.double(0),
          noiseTermLowE = cms.double(0),
          threshHighE = cms.double(-1),
          threshLowE = cms.double(-1)
        )
      ),
      positionCalc = cms.PSet(
        algoName = cms.string(''),
        minFractionInCalc = cms.double(0),
        posCalcNCrystals = cms.int32(-1),
        logWeightDenominatorByDetector = cms.VPSet(
        ),
        logWeightDenominator = cms.double(0),
        minAllowedNormalization = cms.double(0),
        timeResolutionCalcBarrel = cms.PSet(
          constantTerm = cms.double(0),
          constantTermLowE = cms.double(0),
          corrTermLowE = cms.double(0),
          noiseTerm = cms.double(0),
          noiseTermLowE = cms.double(0),
          threshHighE = cms.double(-1),
          threshLowE = cms.double(-1)
        ),
        timeResolutionCalcEndcap = cms.PSet(
          constantTerm = cms.double(0),
          constantTermLowE = cms.double(0),
          corrTermLowE = cms.double(0),
          noiseTerm = cms.double(0),
          noiseTermLowE = cms.double(0),
          threshHighE = cms.double(-1),
          threshLowE = cms.double(-1)
        )
      ),
      minFractionToKeep = cms.double(0),
      nSigmaEta = cms.double(0),
      nSigmaPhi = cms.double(0),
      excludeOtherSeeds = cms.bool(False),
      maxIterations = cms.uint32(0),
      minFracTot = cms.double(0),
      positionCalcForConvergence = cms.PSet(
        algoName = cms.string(''),
        minFractionInCalc = cms.double(0),
        T0_EB = cms.double(0),
        T0_EE = cms.double(0),
        T0_ES = cms.double(0),
        W0 = cms.double(0),
        X0 = cms.double(0),
        minAllowedNormalization = cms.double(0),
        timeResolutionCalc = cms.PSet()
      ),
      recHitEnergyNorms = cms.VPSet(
      ),
      showerSigma = cms.double(1.5),
      stoppingTolerance = cms.double(1e-08),
      clusterTimeResFromSeed = cms.bool(False),
      maxNSigmaTime = cms.double(10),
      minChi2Prob = cms.double(0),
      timeResolutionCalcBarrel = cms.PSet(
        constantTerm = cms.double(0),
        constantTermLowE = cms.double(0),
        corrTermLowE = cms.double(0),
        noiseTerm = cms.double(0),
        noiseTermLowE = cms.double(0),
        threshHighE = cms.double(-1),
        threshLowE = cms.double(-1)
      ),
      timeResolutionCalcEndcap = cms.PSet(
        constantTerm = cms.double(0),
        constantTermLowE = cms.double(0),
        corrTermLowE = cms.double(0),
        noiseTerm = cms.double(0),
        noiseTermLowE = cms.double(0),
        threshHighE = cms.double(-1),
        threshLowE = cms.double(-1)
      ),
      timeSigmaEB = cms.double(10),
      timeSigmaEE = cms.double(10)
    ),
    positionReCalc = cms.PSet(
      algoName = cms.string(''),
      minFractionInCalc = cms.double(0),
      updateTiming = cms.bool(False),
      T0_EB = cms.double(0),
      T0_EE = cms.double(0),
      T0_ES = cms.double(0),
      W0 = cms.double(0),
      X0 = cms.double(0),
      minAllowedNormalization = cms.double(0),
      timeResolutionCalc = cms.PSet()
    ),
    energyCorrector = cms.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
