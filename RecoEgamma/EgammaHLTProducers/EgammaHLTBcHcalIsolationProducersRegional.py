import FWCore.ParameterSet.Config as cms

def EgammaHLTBcHcalIsolationProducersRegional(*args, **kwargs):
  mod = cms.EDProducer('EgammaHLTBcHcalIsolationProducersRegional',
    recoEcalCandidateProducer = cms.InputTag('hltRecoEcalCandidate'),
    caloTowerProducer = cms.InputTag('hltTowerMakerForAll'),
    rhoProducer = cms.InputTag('fixedGridRhoFastjetAllCalo'),
    doRhoCorrection = cms.bool(False),
    rhoMax = cms.double(999999),
    rhoScale = cms.double(1),
    etMin = cms.double(-1),
    innerCone = cms.double(0),
    outerCone = cms.double(0.15),
    depth = cms.int32(-1),
    doEtSum = cms.bool(False),
    useSingleTower = cms.bool(False),
    effectiveAreas = cms.vdouble(
      0.079,
      0.25
    ),
    absEtaLowEdges = cms.vdouble(
      0,
      1.479
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
