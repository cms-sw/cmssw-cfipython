import FWCore.ParameterSet.Config as cms

def OnlineMetaDataRawToDigi(**kwargs):
  mod = cms.EDProducer('OnlineMetaDataRawToDigi',
    onlineMetaDataInputLabel = cms.InputTag('rawDataCollector'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
