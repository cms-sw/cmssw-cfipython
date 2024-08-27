import FWCore.ParameterSet.Config as cms

def RawDataMapperByLabel(**kwargs):
  mod = cms.EDProducer('RawDataMapperByLabel',
    rawCollectionList = cms.VInputTag(
      'rawDataCollector::@skipCurrentProcess',
      'rawDataRepacker',
      'rawPrimeDataRepacker',
      'rawDataReducedFormat'
    ),
    mainCollection = cms.InputTag('rawDataCollector'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
