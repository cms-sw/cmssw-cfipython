import FWCore.ParameterSet.Config as cms

pfeGammaToCandidate = cms.EDProducer('PFEGammaToCandidate',
  photons = cms.InputTag('selectedPatPhotons'),
  electrons = cms.InputTag('selectedPatElectrons'),
  photon2pf = cms.InputTag('particleBasedIsolation', 'gedPhotons'),
  electron2pf = cms.InputTag('particleBasedIsolation', 'gedGsfElectrons')
)
