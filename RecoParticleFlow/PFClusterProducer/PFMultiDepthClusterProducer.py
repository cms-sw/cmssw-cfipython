import FWCore.ParameterSet.Config as cms

def PFMultiDepthClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('PFMultiDepthClusterProducer',
    clustersSource = cms.InputTag(''),
    energyCorrector = cms.PSet(),
    pfClusterBuilder = cms.PSet(
      algoName = cms.string('PFMultiDepthClusterizer'),
      allCellsPositionCalc = cms.PSet(
        algoName = cms.string('Basic2DGenericPFlowPositionCalc'),
        logWeightDenominatorByDetector = cms.VPSet(
        ),
        minAllowedNormalization = cms.double(1e-09),
        minFractionInCalc = cms.double(1e-09),
        posCalcNCrystals = cms.int32(-1),
        timeResolutionCalcBarrel = cms.PSet(),
        timeResolutionCalcEndcap = cms.PSet()
      ),
      positionCalc = cms.PSet(),
      minFractionToKeep = cms.double(1e-07),
      nSigmaEta = cms.double(2),
      nSigmaPhi = cms.double(2)
    ),
    positionReCalc = cms.PSet(),
    usePFThresholdsFromDB = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
