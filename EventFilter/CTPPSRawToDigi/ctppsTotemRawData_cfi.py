import FWCore.ParameterSet.Config as cms

ctppsTotemRawData = cms.EDProducer('CTPPSTotemDigiToRaw',
  InputLabel = cms.InputTag('RPSiDetDigitizer'),
  mightGet = cms.optional.untracked.vstring
)
