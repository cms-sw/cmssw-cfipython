import FWCore.ParameterSet.Config as cms

rawDataMapperByLabel = cms.EDProducer('RawDataMapperByLabel',
  rawCollectionList = cms.VInputTag(
    'rawDataCollector::@skipCurrentProcess',
    'rawDataRepacker',
    'rawPrimeDataRepacker',
    'rawDataReducedFormat'
  ),
  mainCollection = cms.InputTag('rawDataCollector'),
  mightGet = cms.optional.untracked.vstring
)
