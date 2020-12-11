import FWCore.ParameterSet.Config as cms

caloparticlevalidationDefault = cms.EDProducer('CaloParticleValidation',
  folder = cms.string('HGCAL/'),
  simPFClusters = cms.InputTag('simPFProducer', 'perfect'),
  simPFCandidates = cms.InputTag('simPFProducer'),
  mightGet = cms.optional.untracked.vstring
)
