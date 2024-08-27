import FWCore.ParameterSet.Config as cms

def EgammaHLTHcalVarProducerFromRecHit(**kwargs):
  mod = cms.EDProducer('EgammaHLTHcalVarProducerFromRecHit',
    recoEcalCandidateProducer = cms.InputTag('hltRecoEcalCandidate'),
    rhoProducer = cms.InputTag('fixedGridRhoFastjetAllCalo'),
    hbheRecHitsTag = cms.InputTag('hltHbhereco'),
    doRhoCorrection = cms.bool(False),
    rhoMax = cms.double(999999),
    rhoScale = cms.double(1),
    eThresHB = cms.vdouble(
      0.1,
      0.2,
      0.3,
      0.3
    ),
    etThresHB = cms.vdouble(
      0,
      0,
      0,
      0
    ),
    eThresHE = cms.vdouble(
      0.1,
      0.2,
      0.2,
      0.2,
      0.2,
      0.2,
      0.2
    ),
    etThresHE = cms.vdouble(
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ),
    usePFThresholdsFromDB = cms.bool(True),
    innerCone = cms.double(0),
    outerCone = cms.double(0.14),
    depth = cms.int32(0),
    maxSeverityHB = cms.int32(9),
    maxSeverityHE = cms.int32(9),
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
