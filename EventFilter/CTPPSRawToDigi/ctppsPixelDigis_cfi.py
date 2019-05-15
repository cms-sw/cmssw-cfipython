import FWCore.ParameterSet.Config as cms

ctppsPixelDigis = cms.EDProducer('CTPPSPixelRawToDigi',
  includeErrors = cms.bool(True),
  inputLabel = cms.InputTag('rawDataCollector'),
  mappingLabel = cms.string('RPix')
)
