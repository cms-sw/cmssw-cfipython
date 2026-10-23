import FWCore.ParameterSet.Config as cms

def ElectronMVANtuplizer(*args, **kwargs):
  mod = cms.EDAnalyzer('ElectronMVANtuplizer',
    src = cms.InputTag('slimmedElectrons'),
    vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
    pileup = cms.InputTag('slimmedAddPileupInfo'),
    genParticles = cms.InputTag('prunedGenParticles'),
    ebReducedRecHitCollection = cms.InputTag('reducedEgamma', 'reducedEBRecHits'),
    eeReducedRecHitCollection = cms.InputTag('reducedEgamma', 'reducedEERecHits'),
    variableDefinition = cms.required.string,
    doEnergyMatrix = cms.bool(False),
    energyMatrixSize = cms.int32(2),
    isMC = cms.bool(True),
    deltaR = cms.double(0.1),
    ptThreshold = cms.double(5),
    eleMVAs = cms.vstring(),
    eleMVALabels = cms.vstring(),
    eleMVAValMaps = cms.vstring(),
    eleMVAValMapLabels = cms.vstring(),
    eleMVACats = cms.vstring(),
    eleMVACatLabels = cms.vstring(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
