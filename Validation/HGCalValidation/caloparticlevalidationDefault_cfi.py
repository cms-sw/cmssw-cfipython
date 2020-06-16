import FWCore.ParameterSet.Config as cms

caloparticlevalidationDefault = cms.EDProducer('CaloParticleValidation',
  folder = cms.string('HGCAL/'),
  particles_to_monitor = cms.vint32(
    11,
    -11,
    13,
    -13,
    22,
    111,
    211,
    -211,
    321,
    -321
  ),
  simVertices = cms.InputTag('g4SimHits'),
  caloParticles = cms.InputTag('mix', 'MergedCaloTruth'),
  simPFClusters = cms.InputTag('simPFProducer', 'perfect'),
  simPFCandidates = cms.InputTag('simPFProducer'),
  hitMapTag = cms.InputTag('hgcalRecHitMapProducer'),
  mightGet = cms.optional.untracked.vstring
)
