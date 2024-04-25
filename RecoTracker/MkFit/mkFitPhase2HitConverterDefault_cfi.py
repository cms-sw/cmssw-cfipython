import FWCore.ParameterSet.Config as cms

mkFitPhase2HitConverterDefault = cms.EDProducer('MkFitPhase2HitConverter',
  siPhase2Hits = cms.InputTag('siPhase2RecHits'),
  ttrhBuilder = cms.ESInputTag('', 'WithTrackAngle'),
  mightGet = cms.optional.untracked.vstring
)
