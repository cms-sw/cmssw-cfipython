import FWCore.ParameterSet.Config as cms

def PluginUsingProducer(**kwargs):
  mod = cms.EDProducer('PluginUsingProducer',
    plugin = cms.PSet(
      value = cms.int32(5),
      type = cms.string('edmtestValueMaker')
    
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
