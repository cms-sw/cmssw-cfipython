import FWCore.ParameterSet.Config as cms

ctppsPixelRawData = cms.EDProducer('CTPPSPixelDigiToRaw',
  InputLabel = cms.InputTag('RPixDetDigitizer'),
  mappingLabel = cms.string('RPix'),
  mightGet = cms.optional.untracked.vstring
)
