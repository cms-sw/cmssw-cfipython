import FWCore.ParameterSet.Config as cms

def CaloParticleValidation(*args, **kwargs):
  mod = cms.EDProducer('CaloParticleValidation',
    folder = cms.string('HGCAL/'),
    simPFClusters = cms.InputTag('simPFProducer', 'perfect'),
    simPFCandidates = cms.InputTag('simPFProducer'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
