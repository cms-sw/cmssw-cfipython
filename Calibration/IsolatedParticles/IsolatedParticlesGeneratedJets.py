import FWCore.ParameterSet.Config as cms

def IsolatedParticlesGeneratedJets(**kwargs):
  mod = cms.EDAnalyzer('IsolatedParticlesGeneratedJets',
    Debug = cms.untracked.bool(True),
    JetSource = cms.InputTag('ak5GenJets'),
    ParticleSource = cms.InputTag('genParticles'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
