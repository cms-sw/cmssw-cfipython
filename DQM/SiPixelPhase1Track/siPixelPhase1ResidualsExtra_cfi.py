import FWCore.ParameterSet.Config as cms

siPixelPhase1ResidualsExtra = cms.EDProducer('SiPixelPhase1ResidualsExtra',
  TopFolderName = cms.string('PixelPhase1/Tracks/ResidualsExtra'),
  InputFolderName = cms.string(''),
  MinHits = cms.int32(30),
  mightGet = cms.optional.untracked.vstring
)
