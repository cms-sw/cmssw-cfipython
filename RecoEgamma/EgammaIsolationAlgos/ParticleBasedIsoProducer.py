import FWCore.ParameterSet.Config as cms

def ParticleBasedIsoProducer(*args, **kwargs):
  mod = cms.EDProducer('ParticleBasedIsoProducer',
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
