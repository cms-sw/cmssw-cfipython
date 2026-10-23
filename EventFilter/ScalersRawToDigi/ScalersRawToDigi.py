import FWCore.ParameterSet.Config as cms

def ScalersRawToDigi(*args, **kwargs):
  mod = cms.EDProducer('ScalersRawToDigi',
    scalersInputTag = cms.InputTag('rawDataCollector'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
