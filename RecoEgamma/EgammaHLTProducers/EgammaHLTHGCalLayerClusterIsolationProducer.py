import FWCore.ParameterSet.Config as cms

def EgammaHLTHGCalLayerClusterIsolationProducer(**kwargs):
  mod = cms.EDProducer('EgammaHLTHGCalLayerClusterIsolationProducer',
    recoEcalCandidateProducer = cms.InputTag('hltL1SeededRecoEcalCandidatePF'),
    layerClusterProducer = cms.InputTag('hltParticleFlowClusterECAL'),
    rhoProducer = cms.InputTag('fixedGridRhoFastjetAllCalo'),
    doRhoCorrection = cms.bool(False),
    useEt = cms.bool(False),
    rhoMax = cms.double(99999999),
    rhoScale = cms.double(1),
    drMax = cms.double(0.3),
    drVetoEM = cms.double(0),
    drVetoHad = cms.double(0),
    minEnergyEM = cms.double(0),
    minEnergyHad = cms.double(0),
    minEtEM = cms.double(0),
    minEtHad = cms.double(0),
    effectiveAreas = cms.vdouble(
      0,
      0
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
