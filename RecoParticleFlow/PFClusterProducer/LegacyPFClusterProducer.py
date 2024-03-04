import FWCore.ParameterSet.Config as cms

def LegacyPFClusterProducer(**kwargs):
  mod = cms.EDProducer('LegacyPFClusterProducer',
    src = cms.InputTag('pfClusterSoAProducer'),
    PFRecHitsLabelIn = cms.InputTag('pfRecHitSoAProducerHCAL'),
    recHitsSource = cms.InputTag('legacyPFRecHitProducer'),
    usePFThresholdsFromDB = cms.bool(True),
    pfClusterBuilder = cms.PSet(
      maxIterations = cms.uint32(5),
      minFracTot = cms.double(1e-20),
      minFractionToKeep = cms.double(1e-07),
      excludeOtherSeeds = cms.bool(True),
      showerSigma = cms.double(10),
      stoppingTolerance = cms.double(1e-08),
      timeSigmaEB = cms.double(10),
      timeSigmaEE = cms.double(10),
      maxNSigmaTime = cms.double(10),
      minChi2Prob = cms.double(0),
      clusterTimeResFromSeed = cms.bool(False),
      algoName = cms.string(''),
      recHitEnergyNorms = cms.VPSet(
        cms.PSet(
          depths = cms.vint32(
            1,
            2,
            3,
            4
          ),
          detector = cms.string('HCAL_BARREL1'),
          recHitEnergyNorm = cms.vdouble(
            0.1,
            0.2,
            0.3,
            0.3
          )
        ),
        cms.PSet(
          depths = cms.vint32(
            1,
            2,
            3,
            4,
            5,
            6,
            7
          ),
          detector = cms.string('HCAL_ENDCAP'),
          recHitEnergyNorm = cms.vdouble(
            0.1,
            0.2,
            0.2,
            0.2,
            0.2,
            0.2,
            0.2
          )
        )
      ),
      positionCalc = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
        minFractionInCalc = cms.double(1e-09),
        posCalcNCrystals = cms.int32(5),
        logWeightDenominatorByDetector = cms.VPSet(
          cms.PSet(
            depths = cms.vint32(
              1,
              2,
              3,
              4
            ),
            detector = cms.string('HCAL_BARREL1'),
            logWeightDenominator = cms.vdouble(
              0.1,
              0.2,
              0.3,
              0.3
            )
          ),
          cms.PSet(
            depths = cms.vint32(
              1,
              2,
              3,
              4,
              5,
              6,
              7
            ),
            detector = cms.string('HCAL_ENDCAP'),
            logWeightDenominator = cms.vdouble(
              0.1,
              0.2,
              0.2,
              0.2,
              0.2,
              0.2,
              0.2
            )
          )
        ),
        minAllowedNormalization = cms.double(1e-09)
      ),
      allCellsPositionCalc = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
        minFractionInCalc = cms.double(1e-09),
        posCalcNCrystals = cms.int32(-1),
        logWeightDenominatorByDetector = cms.VPSet(
          cms.PSet(
            depths = cms.vint32(
              1,
              2,
              3,
              4
            ),
            detector = cms.string('HCAL_BARREL1'),
            logWeightDenominator = cms.vdouble(
              0.1,
              0.2,
              0.3,
              0.3
            )
          ),
          cms.PSet(
            depths = cms.vint32(
              1,
              2,
              3,
              4,
              5,
              6,
              7
            ),
            detector = cms.string('HCAL_ENDCAP'),
            logWeightDenominator = cms.vdouble(
              0.1,
              0.2,
              0.2,
              0.2,
              0.2,
              0.2,
              0.2
            )
          )
        ),
        minAllowedNormalization = cms.double(1e-09)
      ),
      timeResolutionCalcBarrel = cms.PSet(
        corrTermLowE = cms.double(0),
        threshLowE = cms.double(6),
        noiseTerm = cms.double(21.86),
        constantTermLowE = cms.double(4.24),
        noiseTermLowE = cms.double(8),
        threshHighE = cms.double(15),
        constantTerm = cms.double(2.82)
      ),
      timeResolutionCalcEndcap = cms.PSet(
        corrTermLowE = cms.double(0),
        threshLowE = cms.double(6),
        noiseTerm = cms.double(21.86),
        constantTermLowE = cms.double(4.24),
        noiseTermLowE = cms.double(8),
        threshHighE = cms.double(15),
        constantTerm = cms.double(2.82)
      ),
      positionReCalc = cms.PSet(),
      energyCorrector = cms.PSet()
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
