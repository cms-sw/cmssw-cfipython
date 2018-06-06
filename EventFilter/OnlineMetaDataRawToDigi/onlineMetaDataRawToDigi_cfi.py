import FWCore.ParameterSet.Config as cms

onlineMetaDataRawToDigi = cms.EDProducer('OnlineMetaDataRawToDigi',
  onlineMetaDataInputLabel = cms.InputTag('rawDataCollector')
)
