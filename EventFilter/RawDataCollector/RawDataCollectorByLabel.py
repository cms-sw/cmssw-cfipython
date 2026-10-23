import FWCore.ParameterSet.Config as cms

def RawDataCollectorByLabel(*args, **kwargs):
  mod = cms.EDProducer('RawDataCollectorByLabel',
    RawCollectionList = cms.VInputTag(
      'SiStripDigiToZSRaw',
      'rawDataCollector'
    ),
    verbose = cms.untracked.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
