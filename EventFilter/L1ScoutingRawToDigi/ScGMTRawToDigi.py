import FWCore.ParameterSet.Config as cms

def ScGMTRawToDigi(**kwargs):
  mod = cms.EDProducer('ScGMTRawToDigi',
    srcInputTag = cms.InputTag('rawDataCollector'),
    skipInterm = cms.bool(True),
    debug = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
