import FWCore.ParameterSet.Config as cms

def OnlineMetaDataRawToDigi(*args, **kwargs):
  mod = cms.EDProducer('OnlineMetaDataRawToDigi',
    onlineMetaDataInputLabel = cms.InputTag('rawDataCollector'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
