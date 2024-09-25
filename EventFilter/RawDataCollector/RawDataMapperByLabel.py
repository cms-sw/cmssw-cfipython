import FWCore.ParameterSet.Config as cms

def RawDataMapperByLabel(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
