import FWCore.ParameterSet.Config as cms

def PhotonMVANtuplizer(**kwargs):
  mod = cms.EDAnalyzer('PhotonMVANtuplizer',
    src = cms.InputTag('slimmedPhotons'),
    vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
    pileup = cms.InputTag('slimmedAddPileupInfo'),
    genParticles = cms.InputTag('prunedGenParticles'),
    ebReducedRecHitCollection = cms.InputTag('reducedEgamma', 'reducedEBRecHits'),
    eeReducedRecHitCollection = cms.InputTag('reducedEgamma', 'reducedEERecHits'),
    phoMVAs = cms.vstring(),
    phoMVALabels = cms.vstring(),
    phoMVAValMaps = cms.vstring(),
    phoMVAValMapLabels = cms.vstring(),
    phoMVACats = cms.vstring(),
    phoMVACatLabels = cms.vstring(),
    doEnergyMatrix = cms.bool(False),
    energyMatrixSize = cms.int32(2),
    isMC = cms.bool(True),
    ptThreshold = cms.double(15),
    deltaR = cms.double(0.1),
    variableDefinition = cms.required.string,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
