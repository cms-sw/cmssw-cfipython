import FWCore.ParameterSet.Config as cms

siPixelRawData = cms.EDProducer('SiPixelDigiToRaw',
  InputLabel = cms.required.InputTag,
  UsePhase1 = cms.bool(False),
  Timing = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
