import FWCore.ParameterSet.Config as cms

def PFClusterParamsESProducer_alpaka(**kwargs):
  mod = cms.ESProducer('PFClusterParamsESProducer@alpaka',
    seedFinder = cms.PSet(
      nNeighbours = cms.int32(4),
      thresholdsByDetector = cms.VPSet(
        cms.PSet(
          detector = cms.string('HCAL_BARREL1'),
          seedingThreshold = cms.vdouble(
            0.125,
            0.25,
            0.35,
            0.35
          ),
          seedingThresholdPt = cms.double(0)
        ),
        cms.PSet(
          detector = cms.string('HCAL_ENDCAP'),
          seedingThreshold = cms.vdouble(
            0.1375,
            0.275,
            0.275,
            0.275,
            0.275,
            0.275,
            0.275
          ),
          seedingThresholdPt = cms.double(0)
        )
      )
    ),
    initialClusteringStep = cms.PSet(
      thresholdsByDetector = cms.VPSet(
        cms.PSet(
          detector = cms.string('HCAL_BARREL1'),
          gatheringThreshold = cms.vdouble(
            0.1,
            0.2,
            0.3,
            0.3
          )
        ),
        cms.PSet(
          detector = cms.string('HCAL_ENDCAP'),
          gatheringThreshold = cms.vdouble(
            0.1,
            0.2,
            0.2,
            0.2,
            0.2,
            0.2,
            0.2
          )
        )
      )
    ),
    pfClusterBuilder = cms.PSet(
      maxIterations = cms.uint32(50),
      minFracTot = cms.double(1e-20),
      minFractionToKeep = cms.double(1e-07),
      excludeOtherSeeds = cms.bool(True),
      showerSigma = cms.double(10),
      stoppingTolerance = cms.double(1e-08),
      recHitEnergyNorms = cms.VPSet(
        cms.PSet(
          detector = cms.string('HCAL_BARREL1'),
          recHitEnergyNorm = cms.vdouble(
            0.1,
            0.2,
            0.3,
            0.3
          )
        ),
        cms.PSet(
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
        minFractionInCalc = cms.double(1e-09),
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
      )
    ),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
