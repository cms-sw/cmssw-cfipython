import FWCore.ParameterSet.Config as cms

siPixelRawData = cms.EDProducer('SiPixelDigiToRaw',
  UsePhase1 = cms.bool(False),
  Timing = cms.untracked.bool(False)
)
