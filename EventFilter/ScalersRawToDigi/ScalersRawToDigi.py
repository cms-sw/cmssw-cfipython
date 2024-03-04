import FWCore.ParameterSet.Config as cms

def ScalersRawToDigi(**kwargs):
  mod = cms.EDProducer('ScalersRawToDigi',
    scalersInputTag = cms.InputTag('rawDataCollector'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
