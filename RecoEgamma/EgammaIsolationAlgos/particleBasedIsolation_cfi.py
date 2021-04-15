import FWCore.ParameterSet.Config as cms

particleBasedIsolation = cms.EDProducer('ParticleBasedIsoProducer',
  valueMapEleToEG = cms.string(''),
  valueMapPhoToEG = cms.string('valMapPFEgammaCandToPhoton'),
  electronTmpProducer = cms.InputTag('gedGsfElectronsTmp'),
  pfCandidates = cms.InputTag('particleFlow'),
  valueMapElePFblockIso = cms.string('gedGsfElectrons'),
  electronProducer = cms.InputTag('gedGsfElectrons'),
  photonTmpProducer = cms.InputTag('gedPhotonsTmp'),
  pfEgammaCandidates = cms.InputTag('particleFlowEGamma'),
  pfBlockBasedIsolationSetUp = cms.PSet(
    ComponentName = cms.string('pfBlockBasedIsolation'),
    coneSize = cms.double(9999999999)
  ),
  photonProducer = cms.InputTag('gedPhotons'),
  valueMapPhoPFblockIso = cms.string('gedPhotons'),
  mightGet = cms.optional.untracked.vstring
)
