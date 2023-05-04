import FWCore.ParameterSet.Config as cms

scalersRawToDigi = cms.EDProducer('ScalersRawToDigi',
  scalersInputTag = cms.InputTag('rawDataCollector'),
  mightGet = cms.optional.untracked.vstring
)
