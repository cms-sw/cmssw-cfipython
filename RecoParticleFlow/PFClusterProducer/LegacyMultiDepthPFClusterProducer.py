import FWCore.ParameterSet.Config as cms

def LegacyMultiDepthPFClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('LegacyMultiDepthPFClusterProducer',
    pfClusterSoA = cms.InputTag('pfClusterSoAProducer'),
    pfRecHitFractionSoA = cms.InputTag('pfClusterSoAProducer'),
    pfRecHitsSoA = cms.InputTag('pfRecHitSoAProducerHCAL'),
    recHitsSource = cms.InputTag('legacyPFRecHitProducer'),
    usePFThresholdsFromDB = cms.bool(True),
    energyCorrector = cms.PSet(),
    pfClusterBuilder = cms.PSet(
      algoName = cms.string('PFMultiDepthClusterizer'),
      allCellsPositionCalc = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
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
          ),
          template = cms.PSetTemplate(
            detector = cms.string(''),
            depths = cms.vint32(),
            logWeightDenominator = cms.vdouble()
          )
        ),
        minAllowedNormalization = cms.double(1e-09),
        minFractionInCalc = cms.double(1e-09),
        posCalcNCrystals = cms.int32(-1),
        timeResolutionCalcBarrel = cms.PSet(),
        timeResolutionCalcEndcap = cms.PSet()
      ),
      positionCalc = cms.PSet(),
      minFractionToKeep = cms.double(1e-07)
    ),
    positionReCalc = cms.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
