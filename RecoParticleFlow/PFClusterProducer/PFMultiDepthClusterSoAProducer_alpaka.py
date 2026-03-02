import FWCore.ParameterSet.Config as cms

def PFMultiDepthClusterSoAProducer_alpaka(*args, **kwargs):
  mod = cms.EDProducer('PFMultiDepthClusterSoAProducer@alpaka',
    clustersSrc = cms.InputTag(''),
    rhfracSrc = cms.InputTag(''),
    rechitSrc = cms.InputTag(''),
    nSigmaEta = cms.double(2),
    nSigmaPhi = cms.double(2),
    energyCorrector = cms.PSet(),
    pfClusterBuilder = cms.PSet(
      algoName = cms.string('PFMultiDepthClusterizer'),
      allCellsPositionCalc = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
        logWeightDenominatorByDetector = cms.VPSet(
          template = cms.PSetTemplate(
            depths = cms.vint32(),
            detector = cms.string(''),
            logWeightDenominator = cms.vdouble()
          )
        ),
        minAllowedNormalization = cms.double(1e-09),
        minFractionInCalc = cms.double(1e-09),
        posCalcNCrystals = cms.int32(-1),
        timeResolutionCalcBarrel = cms.PSet(),
        timeResolutionCalcEndcap = cms.PSet()
      ),
      minFractionToKeep = cms.double(1e-07),
      nSigmaEta = cms.double(2),
      nSigmaPhi = cms.double(2)
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
