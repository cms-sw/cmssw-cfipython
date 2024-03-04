import FWCore.ParameterSet.Config as cms

def PFEGammaToCandidate(**kwargs):
  mod = cms.EDProducer('PFEGammaToCandidate',
    photons = cms.InputTag('selectedPatPhotons'),
    electrons = cms.InputTag('selectedPatElectrons'),
    photon2pf = cms.InputTag('particleBasedIsolation', 'gedPhotons'),
    electron2pf = cms.InputTag('particleBasedIsolation', 'gedGsfElectrons'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
