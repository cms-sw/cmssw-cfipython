import FWCore.ParameterSet.Config as cms

particleTowerProducer = cms.EDProducer('ParticleTowerProducer',
  src = cms.InputTag('particleFlow'),
  useHF = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
