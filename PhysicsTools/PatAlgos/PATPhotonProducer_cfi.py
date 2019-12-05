import FWCore.ParameterSet.Config as cms

PATPhotonProducer = cms.EDProducer('PATPhotonProducer',
  photonSource = cms.InputTag('no default'),
  embedSuperCluster = cms.bool(True),
  addGenMatch = cms.bool(True),
  embedGenMatch = cms.bool(False),
  genParticleMatch = cms.InputTag(''),
  addResolutions = cms.bool(False),
  resolutions = cms.PSet(),
  addPhotonID = cms.bool(True),
  photonIDSource = cms.InputTag(''),
  isoDeposits = cms.PSet(),
  efficiencies = cms.PSet(),
  addEfficiencies = cms.bool(False),
  userData = cms.PSet(
    userClasses = cms.PSet(),
    userFloats = cms.PSet(),
    userInts = cms.PSet(),
    userCands = cms.PSet(),
    userFunctions = cms.vstring(),
    userFunctionLabels = cms.vstring()
  ),
  userIsolation = cms.PSet()
)
