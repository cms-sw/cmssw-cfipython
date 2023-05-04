import FWCore.ParameterSet.Config as cms

alignmentPrescaler = cms.EDProducer('AlignmentPrescaler',
  src = cms.InputTag('generalTracks'),
  assomap = cms.InputTag('OverlapAssoMap'),
  PrescFileName = cms.string('PrescaleFactors.root'),
  PrescTreeName = cms.string('AlignmentHitMap'),
  mightGet = cms.optional.untracked.vstring
)
