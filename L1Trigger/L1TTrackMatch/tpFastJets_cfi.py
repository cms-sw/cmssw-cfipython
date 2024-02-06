import FWCore.ParameterSet.Config as cms

tpFastJets = cms.EDProducer('TPFastJetProducer',
  TrackingParticleInputTag = cms.InputTag('mix', 'MergedTrackTruth'),
  MCTruthStubInputTag = cms.InputTag('TTStubAssociatorFromPixelDigis', 'StubAccepted'),
  tp_ptMin = cms.double(2),
  tp_etaMax = cms.double(2.4),
  tp_zMax = cms.double(15),
  tp_nStubMin = cms.int32(4),
  tp_nStubLayerMin = cms.int32(4),
  coneSize = cms.double(0.4),
  mightGet = cms.optional.untracked.vstring
)
