import FWCore.ParameterSet.Config as cms

ctppsPixelRawData = cms.EDProducer('CTPPSPixelDigiToRaw',
  isRun3 = cms.bool(True),
  InputLabel = cms.InputTag('RPixDetDigitizer'),
  mappingLabel = cms.string('RPix'),
  mightGet = cms.optional.untracked.vstring
)
