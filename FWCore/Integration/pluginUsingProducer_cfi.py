import FWCore.ParameterSet.Config as cms

pluginUsingProducer = cms.EDProducer('PluginUsingProducer',
  plugin = cms.PSet(
    value = cms.int32(5),
    type = cms.string('edmtestValueMaker')
  
  ),
  mightGet = cms.optional.untracked.vstring
)
