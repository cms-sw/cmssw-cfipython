import FWCore.ParameterSet.Config as cms

def PluginUsingProducer(*args, **kwargs):
  mod = cms.EDProducer('PluginUsingProducer',
    plugin = cms.PSet(
      value = cms.int32(5),
      type = cms.string('edmtestValueMaker')
    
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
