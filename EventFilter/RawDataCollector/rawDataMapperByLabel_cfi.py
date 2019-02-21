import FWCore.ParameterSet.Config as cms

rawDataMapperByLabel = cms.EDProducer('RawDataMapperByLabel',
  rawCollectionList = cms.VInputTag(
    'rawDataCollector::@skipCurrentProcess',
    'rawDataRepacker',
    'rawDataReducedFormat'
  ),
  mainCollection = cms.InputTag('rawDataCollector')
)
