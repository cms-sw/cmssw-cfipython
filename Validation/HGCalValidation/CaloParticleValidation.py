import FWCore.ParameterSet.Config as cms

def CaloParticleValidation(**kwargs):
  mod = cms.EDProducer('CaloParticleValidation',
    folder = cms.string('HGCAL/'),
    simPFClusters = cms.InputTag('simPFProducer', 'perfect'),
    simPFCandidates = cms.InputTag('simPFProducer'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
