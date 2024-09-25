import FWCore.ParameterSet.Config as cms

def IsolatedParticlesGeneratedJets(*args, **kwargs):
  mod = cms.EDAnalyzer('IsolatedParticlesGeneratedJets',
    Debug = cms.untracked.bool(True),
    JetSource = cms.InputTag('ak5GenJets'),
    ParticleSource = cms.InputTag('genParticles'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
