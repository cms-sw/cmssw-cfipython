import FWCore.ParameterSet.Config as cms

siStripBadComponentInfo = cms.EDProducer('SiStripBadComponentInfo',
  StripQualityLabel = cms.string(''),
  BadComponentsFromFedErrors = cms.PSet(
    Add = cms.bool(False),
    Cutoff = cms.double(0.8),
    LegacyDQMFile = cms.string(''),
    FileRunNumber = cms.uint32(4294967295)
  ),
  mightGet = cms.optional.untracked.vstring
)
