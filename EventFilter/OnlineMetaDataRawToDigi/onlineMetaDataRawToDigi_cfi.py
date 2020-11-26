import FWCore.ParameterSet.Config as cms

onlineMetaDataRawToDigi = cms.EDProducer('OnlineMetaDataRawToDigi',
  onlineMetaDataInputLabel = cms.InputTag('rawDataCollector'),
  mightGet = cms.optional.untracked.vstring
)
