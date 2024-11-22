import FWCore.ParameterSet.Config as cms

def PFEGammaToCandidate(*args, **kwargs):
  mod = cms.EDProducer('PFEGammaToCandidate',
    photons = cms.InputTag('selectedPatPhotons'),
    electrons = cms.InputTag('selectedPatElectrons'),
    photon2pf = cms.InputTag('particleBasedIsolation', 'gedPhotons'),
    electron2pf = cms.InputTag('particleBasedIsolation', 'gedGsfElectrons'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
