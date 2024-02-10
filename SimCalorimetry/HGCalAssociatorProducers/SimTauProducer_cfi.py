import FWCore.ParameterSet.Config as cms

SimTauProducer = cms.EDProducer('SimTauProducer',
  caloParticles = cms.InputTag('mix', 'MergedCaloTruth'),
  genParticles = cms.InputTag('genParticles'),
  genBarcodes = cms.InputTag('genParticles'),
  mightGet = cms.optional.untracked.vstring
)
